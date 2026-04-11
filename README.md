"# Avance Proyecto Final Devops" 
Se diseñó un flujo de trabajo que elimina los procesos manuales, integrando contenedores para la aplicación y un pipeline que prueba y despliega el código automáticamente cada vez que se detecta un cambio

Tecnologias Utilizadas
Infraestructura: AWS (EC2 para el servidor y S3 para almacenamiento).
Contenedores: Docker y Docker Compose para orquestar la App (Flask) y el Proxy (Nginx)
Lenguajes: Python (Backend y Automatización) y Bash (Scripts de sistema)
CI/CD: GitHub Actions para pruebas y despliegue continuo.
IaC: CloudFormation para crear la infraestructura como código

Pipeline
Etapa de Pruebas (Test): Se ejecutan pruebas unitarias con pytest para asegurar que la aplicación funciona correctamente antes de subirla al servidor.
Etapa de Despliegue (Deploy): Si las pruebas pasan, GitHub se conecta por SSH a la instancia de AWS y actualiza los contenedores automáticamente.
Rollback Automático: Si algo falla durante el despliegue, un script de Bash (rollback.sh) devuelve el sistema a la versión anterior estable de inmediato

Como ejecutarlo
Preparar el servidor: Ejecutar el script setup.sh para instalar Docker, Python y dependencias de AWS
Lanzar la infraestructura: Usar la plantilla infra.yaml con CloudFormation para crear recursos en segundos
Desplegar app: Ejecutar sudo docker-compose up -d --build.
