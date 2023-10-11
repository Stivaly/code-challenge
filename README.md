# Proyecto ETL con BigQuery

Este proyecto consiste en un proceso ETL que extrae datos de un archivo CSV, los transforma y los carga en BigQuery. Fue desarrollado usando Python y las herramientas proporcionadas por Google Cloud Platform.


## Estructura del Directorio

codeChallenge/
|-- data/
| |-- source/
| | |-- online_retail.csv
|-- docs/
|-- scripts/
| |-- etl.py
|-- keys/
| |-- etl-code-challenge-42c88c66e88d.json
|-- .gitignore
|-- README.md
|-- requirements.txt 


## Requisitos

- Python 3.11.3
- Google Cloud SDK
- [Otras dependencias se encuentran en `requirements.txt`]

# Referencia de los datos CSV

Online Retail. (2015). UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.

## Configuración del Ambiente

1. **Credenciales de GCP**: Coloque el archivo de credenciales `.json` proporcionado por GCP en el directorio `keys/`.

**Nota importante sobre la clave de servicio**

Por conveniencia y para facilitar la evaluación de este proyecto, he incluido una clave de servicio en el directorio keys. Sin embargo, es esencial destacar que, en un entorno real y de producción, nunca debemos incluir claves de servicio ni ningún otro tipo de credenciales dentro de un repositorio, incluso si es privado.

En la práctica, estas claves deben ser mantenidas fuera del código fuente, y los archivos que las contienen deben ser añadidos al .gitignore para evitar comprometer la seguridad.

2. **Instalar Dependencias**: Ejecute el siguiente comando para instalar todas las dependencias necesarias: pip install -r requirements.txt



## Cómo ejecutar el proceso ETL

1. Navegue en la terminal al directorio principal del proyecto: cd ruta_del_proyecto/codeChallenge
2. Ejecute el script de ETL: codeChallenge/etl.py


## Información Adicional

- 

## Contribuciones

Este proyecto fue desarrollado como parte de un desafío técnico. Cualquier feedback es bienvenido.

## Contacto

Stivaly Gomez - stivaly.g@hotmail.com

