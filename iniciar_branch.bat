@echo off
cd gestor-pyme-branch
echo Creando superusuario admin...
..\.venv\Scripts\python.exe manage.py crear_superusuario
echo.
echo Iniciando servidor Django en puerto 8001...
..\.venv\Scripts\python.exe manage.py runserver 8001
