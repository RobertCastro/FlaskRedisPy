# Usar una imagen base de Node.js
FROM node:14

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar los archivos de definición de dependencias
COPY package*.json ./

# Instalar las dependencias del proyecto
RUN npm install

# Copiar el resto del código fuente del proyecto al directorio de trabajo
COPY . .

# Exponer el puerto en el que el API Gateway se ejecutará
EXPOSE 3000

# Comando para ejecutar el API Gateway
CMD ["node", "gateway.js"]
