# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar los archivos de requisitos primero para aprovechar la caché de capas de Docker
COPY requirements.txt ./

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente del proyecto al directorio de trabajo
COPY . .

# Exponer el puerto en el que la aplicación Flask se ejecutará
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
