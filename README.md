# BackEndTest
Prueba de API usando FastAPI de Python

Para que el ejemplo funciones es necesario instalar la librería FastAPI de python

**Usando conda, definimos el sandbox:** 
- $conda create -n fapi python=3.9.6

**Instalamos las librerías en el entorno vitrual**

- $pip install fastapi
- $pip install requests

**Finalmente instalamos el servidor:**
- $pip install uvicorn

**Activamos el entorno con:**
- $conda activate fapi
- $uvicorn main:app --reload

**Las URLs activas son:**
- Swager: http://127.0.0.1:8000/docs#/default/read_root__get
- Todos los posts (sin convinar con datos de usuario ni comentarios: http://127.0.0.1:8000/
- Listado de posts combinados con datos de usuario y comentarios: http://127.0.0.1:8000/posts/[start]?size=sz
 - [start]: id del punto de partida de los posts a leer (valor numérico)
 - [sz]: tamaño del bloque a leer (valor numérico opcional, en caso de ir vacío usará 10)
