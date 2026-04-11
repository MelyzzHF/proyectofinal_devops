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

echo " Actualizando catálogos del sistem"
sudo apt update -y

echo " Instalando utilidades (Pip, Unzip, Curl"
sudo apt install -y unzip curl

echo "Instalando Boto3 y python3"
sudo apt install -y python3-boto3

echo "Instalando AWS CLI v2 (Método Oficial de Amazon)..."
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -q awscliv2.zip
sudo ./aws/install --update

echo " Instalando Git (Control de Versiones)..."
sudo apt install -y git

echo "Instalación de dependencias completada"
