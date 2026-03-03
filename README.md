# Practica-7-Web-App

Este repositorio contiene una aplicación web "Hola Mundo" que se conecta a una base de datos MySQL usando Docker Compose.

## Estructura del Proyecto
* **src/**: Código fuente de la aplicación Python (Flask).
* **docker-compose.yml**: Definición de los servicios de red, base de datos y servidor web.

## Requisitos
* Docker Desktop instalado y en ejecución.

## Instrucciones de Uso

1. Clonar el repositorio:
   ```bash
   git clone <TU_URL_DE_GITHUB>
   cd my-docker-app
   ```

2. Ejecutar la aplicación con Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Abrir el navegador en: [http://localhost:8080](http://localhost:8080)

## Notas de Configuración
* La base de datos utiliza el usuario `root` con la contraseña `password123`.
* Se mapeó el puerto **8080** para evitar conflictos con AirPlay en macOS.
* Se mapeó el puerto **3307** para evitar conflictos con instancias locales de MySQL.
