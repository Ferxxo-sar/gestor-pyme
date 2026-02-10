Write-Host "Creando superusuario admin..." -ForegroundColor Cyan
.\.venv\Scripts\python.exe manage.py crear_superusuario
Write-Host ""
Write-Host "Iniciando servidor Django..." -ForegroundColor Cyan
.\.venv\Scripts\python.exe manage.py runserver
