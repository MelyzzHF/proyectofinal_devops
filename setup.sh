#!/bin/bash

echo "Actualizando la lista de paquetes"
sudo apt-get update -y

echo "Instalando paquetes esenciales: Git, Vim y Python3"
sudo apt-get install -y git vim python3 python3-pip

echo "Instalando Docker"
sudo apt-get install -y docker.io

echo "Iniciando y habilitando el servicio de Docker"
sudo systemctl start docker
sudo systemctl enable docker

echo "Agregando el usuario actual al grupo de Docker para no requerir sudo"
sudo usermod -aG docker $USER

echo "Instalación de dependencias completada"
