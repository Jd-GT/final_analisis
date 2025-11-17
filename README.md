##  Instalación

Sigue estos pasos **uno por uno** para instalar y configurar el proyecto en tu computadora:

### Paso 1: Clonar el Repositorio

Abre tu terminal (Command Prompt en Windows, Terminal en Mac/Linux) y ejecuta:
`git clone https://github.com/Jd-GT/final_analisis.git`

### Paso 2: Navegar a la Carpeta del Proyecto
`cd final_analisis`

### Paso 3: Crear un Entorno Virtual

**En Windows:**
`python -m venv venv`

**En Mac/Linux:**
`python3 -m venv venv`


### Paso 4: Activar el Entorno Virtual (Opcional)

**En Windows (Command Prompt):**
`venv\Scripts\activate`

**En Windows (PowerShell):**
`venv\Scripts\Activate.ps1`


**En Mac/Linux:**
`source venv/bin/activate`


 **Nota:** Cuando el entorno virtual esté activado, verás `(venv)` al inicio de tu línea de comando.

### Paso 5: Instalar las Dependencias

Con el entorno virtual activado, ejecuta:

`pip install -r requirements.txt`
O
`pip install "django>=4.2,<5.0" "numpy>=1.26,<2.0" "matplotlib>=3.8,<4.0" --upgrade`
O
`pip install asgiref==3.10.0 contourpy==1.3.3 cycler==0.12.1 Django==5.2.7 fonttools==4.60.1 kiwisolver==1.4.9 matplotlib==3.10.7 mpmath==1.3.0 numpy==2.3.4 packaging==25.0 pandas==2.3.3 pillow==12.0.0 pyparsing==3.2.5 python-dateutil==2.9.0.post0 pytz==2025.2 six==1.17.0 sqlparse==0.5.3 sympy==1.14.0 tzdata==2025.2`

Espera a que se instalen todas las librerías necesarias. Esto puede tomar unos minutos.


## 💻 Cómo Usar

### Ejecutar la Aplicación
`python manage.py runserver`


