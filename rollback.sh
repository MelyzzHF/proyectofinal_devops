#!/bin/bash
echo " Error crítico detectado. Iniciando script de Rollback automático..."

# Retrocede un commit en el historial de Git
git reset --hard HEAD~1

# Apaga y vuelve a encender los contenedores con el código anterior
sudo docker compose down
sudo docker compose up -d --build
echo "Rollback completado. El sistema ha sido restaurado a la última versión estable."
