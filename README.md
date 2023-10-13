# Proyecto ETL con BigQuery

Este proyecto consiste en un proceso ETL que extrae datos de un archivo CSV, los transforma y los carga en BigQuery. Fue desarrollado usando Python y las herramientas proporcionadas por Google Cloud Platform. Puedes ingresar al tablero de Jira donde se planificaron y abordaron los scripts en el siguiente link: https://id.atlassian.com/invite/p/jira-software?id=WwbBTysGTx2ZoQookUadeA selecciona *Mi proyecto Kanban* y podrás ingresar al tablero.

## Requisitos

- Python 3.11.3
- Google Cloud SDK
- [Otras dependencias se encuentran en `requirements.txt`]

# Referencia de los datos CSV

Online Retail. (2015). UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.

# Pasos tecnicos

En la carpeta docs del directorio encontrarás la arquitectura de software y el diagrama de flujo que se creo al inicio del proyecto. 

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

## Cómo ejecutar las consultas SQL

Ingresa al siguiente link para ejecutar las consultas de agregación y segmentación del proyecto directamente en BigQuery, luego de ejecutar el proceso ETL: 
    https://console.cloud.google.com/bigquery?sq=877558642730:c95480eb2fbd431d83e9d343fc874147


# Automatización con Task Scheduler en Windows

Para automatizar, debido a que enfrenté muchos inconvenientes configurando tanto airflow como nncron, utilizo el Programador de tareas (Task Scheduler) en Windows. 

## Pasos para programar la automatización:

1. Abre el Programador de tareas de Windows. Puedes encontrarlo en el menú "Herramientas administrativas" o buscarlo en el menú Inicio.

2. En el panel izquierdo, selecciona "Biblioteca del Programador de tareas" para crear una nueva tarea.

3. En la ventana derecha, haz clic en "Crear tarea básica" para comenzar la configuración.

4. Dale un nombre a la tarea y proporciona una descripción opcional. Luego, haz clic en "Siguiente".

5. Selecciona la opción "Diariamente" o elige una frecuencia que se ajuste a tus necesidades y haz clic en "Siguiente".

6. Establece la hora y la fecha en la que deseas que se ejecute la tarea diariamente. Haz clic en "Siguiente".

7. En la siguiente pantalla, selecciona "Iniciar un programa" y haz clic en "Siguiente".

8. En el campo "Programa o script", proporciona la ruta completa al ejecutable de Python del entorno virtual. Ruta relativa desde el repositorio: 
    codeChallenge\venv\Scripts\python.exe

9. En el campo "Agregar argumentos (opcional)", debes proporcionar la ruta del script. Ruta relativa desde el repositorio:
    codeChallenge\src\etl_script.py

10. Haz clic en "Finalizar" para crear la tarea.

11. Verás la tarea en la lista de tareas programadas. Puedes hacer clic derecho en ella y seleccionar "Ejecutar" para probarla de inmediato.

12. La tarea se ejecutará automáticamente según la programación que hayas establecido.


## Información Adicional

*Notas sobre la Carga de Datos en BigQuery*

Durante el proceso, me enfrenté a un desafío inesperado al cargar un archivo de datos en BigQuery. A pesar de que BigQuery es capaz de manejar grandes conjuntos de datos, encontré problemas específicos con el archivo en cuestión. Después de realizar diversas pruebas y diagnósticos, determiné que el problema podría estar relacionado con la calidad, estructura o ciertos registros dentro del archivo. 

Para abordar esta situación, decidí reducir el tamaño del archivo, excluyendo registros problemáticos. Esto me permitió cargar una porción más manejable y limpia del conjunto de datos en BigQuery sin dificultades. Esta estrategia es útil cuando no es práctico analizar detalladamente cada registro en un conjunto de datos grande y se necesita cargar una parte representativa o dividir el archivo en partes iguales para una carga más efectiva.

*Sobre Ramificación y Fusión en Git*

Durante el desarrollo del proyecto, opté por no utilizar la funcionalidad de ramificación y fusión de Git debido a la naturaleza pequeña y directa del proyecto. En lugar de crear ramas adicionales, centré mi enfoque en mantener un flujo de trabajo eficiente mediante la rápida identificación y corrección de errores. 

Aunque reconozco la importancia de las ramas en proyectos más grandes, para este proyecto consideré que podía ofrecer una solución de calidad sin necesidad de utilizarlas. Estoy abierta a la retroalimentación y siempre dispuesta a aprender y mejorar en futuros proyectos.

## Contribuciones

Este proyecto fue desarrollado como parte de un desafío técnico. Cualquier feedback es bienvenido.

## Contacto

Stivaly Gomez - stivaly.g@hotmail.com