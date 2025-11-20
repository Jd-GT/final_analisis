import math
import numpy as np
import pandas as pd

def f_expr(expr, x):
    return eval(expr, {"x": x, "math": math})

def biseccion(fx_str, a, b, tol, niter):
    a, b, tol, niter = float(a), float(b), float(tol), int(niter)
    fa, fb = f_expr(fx_str, a), f_expr(fx_str, b)
    if fa * fb > 0:
        return {"error": "No hay cambio de signo en [a, b]."}
    
    resultados = []
    c_old = None

    for i in range(1, niter + 1):
        c = (a + b) / 2
        fc = f_expr(fx_str, c)

        # Errores
        if c_old is None:
            error_abs = None
            error_rel1 = None
            error_rel2 = None
        else:
            error_abs = abs(c - c_old)
            error_rel1 = abs((c - c_old) / c) if c != 0 else None
            error_rel2 = abs((c - c_old) / c_old) if c_old != 0 else None

        error_cond = None  # No depende de derivada

        resultados.append({
            "iter": i, "a": a, "b": b, "c": c, "f(c)": fc,
            "error_abs": error_abs, "error_rel1": error_rel1,
            "error_rel2": error_rel2, "error_cond": error_cond
        })

        if abs(fc) < tol:
            return {"resultados": resultados, "raiz": c}

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c_old = c

    return {"resultados": resultados, "error": "No converge."}

def punto_fijo(gx_str, x0, tol, niter):
    x0, tol, niter = float(x0), float(tol), int(niter)
    resultados = []
    x_old = None

    for i in range(niter):
        x1 = f_expr(gx_str, x0)

        # Errores
        if x_old is None:
            error_abs = error_rel1 = error_rel2 = None
        else:
            error_abs = abs(x1 - x_old)
            error_rel1 = abs((x1 - x_old) / x1) if x1 != 0 else None
            error_rel2 = abs((x1 - x_old) / x_old) if x_old != 0 else None

        error_cond = None  # no usa derivada

        resultados.append({
            "iter": i + 1, "x0": x0, "x1": x1,
            "error_abs": error_abs, "error_rel1": error_rel1,
            "error_rel2": error_rel2, "error_cond": error_cond
        })

        if error_abs is not None and error_abs < tol:
            return {"resultados": resultados, "raiz": x1}

        x_old = x0
        x0 = x1

    return {"resultados": resultados, "error": "No converge."}

def regla_falsa(fx_str, a, b, tol, niter):
    a, b, tol, niter = float(a), float(b), float(tol), int(niter)
    fa, fb = f_expr(fx_str, a), f_expr(fx_str, b)

    if fa * fb > 0:
        return {"error": "No hay cambio de signo."}

    resultados = []
    c_old = None

    for i in range(1, niter + 1):
        fa, fb = f_expr(fx_str, a), f_expr(fx_str, b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f_expr(fx_str, c)

        # Errores
        if c_old is None:
            error_abs = error_rel1 = error_rel2 = None
        else:
            error_abs = abs(c - c_old)
            error_rel1 = abs((c - c_old) / c) if c != 0 else None
            error_rel2 = abs((c - c_old) / c_old) if c_old != 0 else None

        error_cond = None

        resultados.append({
            "iter": i, "a": a, "b": b, "c": c, "f(c)": fc,
            "error_abs": error_abs, "error_rel1": error_rel1,
            "error_rel2": error_rel2, "error_cond": error_cond
        })

        if abs(fc) < tol:
            return {"resultados": resultados, "raiz": c}

        if fa * fc < 0:
            b = c
        else:
            a = c
        
        c_old = c

    return {"resultados": resultados, "error": "No converge."}

def secante(fx_str, x0, x1, tol, niter):
    resultados = []

    for i in range(niter):
        f0 = f_expr(fx_str, x0)
        f1 = f_expr(fx_str, x1)

        if (f1 - f0) == 0:
            return {"error": "División por cero."}

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        # Errores
        error_abs = abs(x2 - x1)
        error_rel1 = abs((x2 - x1) / x2) if x2 != 0 else None
        error_rel2 = abs((x2 - x1) / x1) if x1 != 0 else None
        error_cond = None  # No usa derivada

        resultados.append({
            "iter": i + 1, "x0": x0, "x1": x1, "x2": x2,
            "error_abs": error_abs, "error_rel1": error_rel1,
            "error_rel2": error_rel2, "error_cond": error_cond
        })

        if error_abs < tol:
            return {"resultados": resultados, "raiz": x2}

        x0, x1 = x1, x2

    return {"resultados": resultados, "error": "No converge."}

def newton(fx_str, dfx_str, x0, tol, niter):
    resultados = []
    x_old = None

    for i in range(niter):
        f = f_expr(fx_str, x0)
        df = f_expr(dfx_str, x0)

        if df == 0:
            return {"error": "Derivada cero."}

        x1 = x0 - f / df

        # Errores
        if x_old is None:
            error_abs = error_rel1 = error_rel2 = None
        else:
            error_abs = abs(x1 - x_old)
            error_rel1 = abs((x1 - x_old) / x1) if x1 != 0 else None
            error_rel2 = abs((x1 - x_old) / x_old) if x_old != 0 else None

        error_cond = abs(df)

        resultados.append({
            "iter": i + 1, "x0": x0, "x1": x1,
            "f(x0)": f, "df(x0)": df,
            "error_abs": error_abs, "error_rel1": error_rel1,
            "error_rel2": error_rel2, "error_cond": error_cond
        })

        if error_abs is not None and error_abs < tol:
            return {"resultados": resultados, "raiz": x1}

        x_old = x0
        x0 = x1

    return {"resultados": resultados, "error": "No converge."}


def raices_multiples(fx_str, dfx_str, ddfx_str, x0, tol, niter):
    x0, tol, niter = float(x0), float(tol), int(niter)
    resultados = []
    x_old = None

    for i in range(1, niter + 1):
        f   = f_expr(fx_str,  x0)
        df  = f_expr(dfx_str, x0)
        ddf = f_expr(ddfx_str, x0)

        denom = df**2 - f * ddf
        if denom == 0:
            return {"error": "Denominador cero."}

        x1 = x0 - (f * df) / denom

        # Errores
        if x_old is None:
            error_abs = error_rel1 = error_rel2 = None
        else:
            error_abs = abs(x1 - x_old)
            error_rel1 = abs((x1 - x_old) / x1) if x1 != 0 else None
            error_rel2 = abs((x1 - x_old) / x_old) if x_old != 0 else None

        error_cond = abs(df)

        resultados.append({
            "iter": i, "x0": x0, "x1": x1,
            "f(x0)": f, "f'(x0)": df, "f''(x0)": ddf,
            "error_abs": error_abs, "error_rel1": error_rel1,
            "error_rel2": error_rel2, "error_cond": error_cond
        })

        if error_abs is not None and error_abs < tol:
            return {"resultados": resultados, "raiz": x1}

        x_old = x0
        x0 = x1

    return {"resultados": resultados, "error": "No converge."}
