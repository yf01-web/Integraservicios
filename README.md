Integraservicios – Proyecto Django

Este es el repositorio del sistema web Integraservicios, desarrollado con Django.




🚀 Requerimientos

Python 3.10+

Git

Pip (administrador de paquetes de Python)

Virtualenv


🧩 Instalación del entorno local
1️⃣ Clonar el repositorio
  git clone https://github.com/TU-USUARIO/TU-REPO.git
  cd TU-REPO
  
2️⃣ Crear un entorno virtual
python -m venv venv

  Activarlo:
  
  Windows:
  
  CMD venv\Scripts\activate (si da error: colocar este comando antes->Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)
  Powershell o en la Terminal de VSCode .\venv\Scripts\Activate.ps1 (si da error: colocar este comando antes->Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)
  
  
  Linux/Mac:
  
  source venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

🛠 4️⃣ Crear la base de datos local

Como db.sqlite3 no está en el repo, cada desarrollador debe crear la suya:

python manage.py makemigrations
python manage.py migrate

5️⃣ Crear un superusuario (para acceder al panel admin)
python manage.py createsuperuser

▶️ 6️⃣ Ejecutar el servidor
python manage.py runserver



El proyecto estará disponible en:
http://127.0.0.1:8000/



