# RMSystem
Micro servicio encargado de simular un dispositivo eléctrico que reporta medidas de manera aleatoria en un rango determinado y almacenarlas en redis stream. Este microservicio tiene el rol de Producer.

El simulador esta construido usando python 3.6 y la libreria asyncio.



Para ejecutar el microservicio localmente.
1. Garantizar que se tiene una instancia de redis corriendo. 
1. Instalar los requerimientos `pip install -r requirements.txt` en un ambiente virtual
2. Ejectar `python exec.py` desde la carpeta `app`


Para ejecutar el microservicio desde docker:
1. levantar el contenedor con el servicio de redis sino se ha levantado aun: [RedisService](https://github.com/OviLuis/RedisService)
1. construir la imagen `producer`. ejecutar `docker build -t producer .` desde la raiz del proyecto donde esta ubicado el archivo `Dockerfile`
2. ejecutar `docker-compose up -d` desde la raiz del proyecto o donde este ubicado el archivo `docker-compose.yml`



