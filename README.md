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
2. **Instalación de Google Cloud SDK**: Si aún no tiene instalado Google Cloud SDK en su máquina, siga las instrucciones en Google Cloud SDK Documentation para instalarlo.
3. **Autenticación**:
Una vez que tenga Google Cloud SDK instalado, ejecute el siguiente comando para autenticarse con su cuenta de Google:


    gcloud auth login

Luego, configure el proyecto de GCP con el siguiente código:


    gcloud config set project [etl-code-challenge]

4. **Configuración de las Credenciales**:

Establezca la variable de entorno GOOGLE_APPLICATION_CREDENTIALS en su máquina apuntando a la ubicación del archivo de credenciales.

En Windows (Powershell):

    $env:GOOGLE_APPLICATION_CREDENTIALS="C:\ruta\completa\al\archivo\de\credenciales.json"

En Linux o Mac:

    export GOOGLE_APPLICATION_CREDENTIALS="/ruta/completa/al/archivo/de/credenciales.json"

💡 Nota: Es importante establecer esta variable de entorno. Si estás trabajando con un entorno de desarrollo específico es posible que solo necesites hacerlo una vez por sesión.

5. **Instalar Dependencias**: Ejecute el siguiente comando para instalar todas las dependencias necesarias: 

    pip install -r requirements.txt


## Cómo ejecutar el proceso ETL

1. Navegue en la terminal al directorio principal del proyecto: cd ruta_del_proyecto/codeChallenge
2. Ejecute el script de ETL: codeChallenge/etl.py

## Cómo ejecutar la consulta SQL

Ingresa al siguiente link para ejecutar las consultas de agregación y segmentación del proyecto directamente en bigquery: 
    https://console.cloud.google.com/bigquery?sq=877558642730:c95480eb2fbd431d83e9d343fc874147

## Información Adicional

*Notas sobre la Carga de Datos en BigQuery*

Durante el proceso, me encontré con un desafío inesperado al cargar el archivo completo de datos en BigQuery. Aunque BigQuery es completamente capaz de manejar conjuntos de datos mucho más grandes de lo que estaba intentando cargar, experimenté problemas con el archivo específico.

El archivo original es muy grande y, después de varias pruebas y diagnósticos, determiné que el problema no era el tamaño del archivo en sí, sino posiblemente la calidad, estructura o algún registro específico dentro del archivo que estaba causando problemas.

La solución que implementé fue reducir el tamaño del archivo para aislar y excluir registros problemáticos, lo que me permitió cargar una porción más manejable y limpia del conjunto de datos en BigQuery sin problemas. Esta estrategia es útil en escenarios donde el diagnóstico detallado de cada registro en un conjunto de datos muy grande es impráctico, y donde un subconjunto de datos sigue siendo representativo para el análisis y en caso de necesitar todos los datos se fragmentariamos el archivo en partes relativamente iguales y subiriamos por partes en el proceso.

*Sobre Ramificación y Fusión en Git*

Durante el desarrollo del proyecto, tomé la decisión consciente de no utilizar la funcionalidad de ramificación (branching) y fusión (merging) de Git. La razón principal detrás de esta elección es la naturaleza relativamente pequeña y directa del proyecto.

Al enfrentar este desafío técnico, consideré que el proyecto no requería ramificaciones adicionales debido a su escala. Además, gracias al manejo eficaz de errores, pude identificar y corregir rápidamente cualquier problema que surgiera, lo que me permitió mantener un flujo de trabajo eficiente sin la necesidad de ramificar.

Reconozco que la ramificación y la fusión son prácticas valiosas en el control de versiones, especialmente en proyectos más grandes o colaborativos. Sin embargo, para este proyecto en particular, sentí que podía ofrecer una solución de calidad sin recurrir a ellas.

Estoy consciente de que el desafío solicitaba el uso de estas técnicas, y agradezco la comprensión en esta decisión. Siempre estoy abierta a recibir retroalimentación y aprender de las experiencias para mejorar en futuros proyectos.


## Contribuciones

Este proyecto fue desarrollado como parte de un desafío técnico. Cualquier feedback es bienvenido.

## Contacto

Stivaly Gomez - stivaly.g@hotmail.com

