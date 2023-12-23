# Empleados

![portada](https://github.com/Origamologo/Empleados/blob/main/images/portada.jpg)

## Descripción
Este trabajo es la prueba técnica dentro del proceso de selección de profesores de Adalab.\
La idea es desarrollar un proceso completo de ETL sobre un conjunto de datos acerca de los trabajadores de una empresa, divididos entre los que está satisfechos con su tradajo y los que abandonaron para irse a trabajar a otro sitio. En los datos encontraremos los motivos que llevan a unos  a quedarse y a otros a marcharse.

## Objetivo
El objetivo de este trabajo es ser el mejor de los candidatos y conseguir la plaza de profesor en Adalab.\
Para lograrlo se hará una lipieza y tratamiento exahustivo de los datos con dos objetivos:

* Realizar un análisis de los datos que nos permita tanto dilucidar las causas de la fuga de talentos y como proponer una estrategia al departamente de recursos humanos.

* Crear una base de datos SQL y automatizar la ingesta de datos con python.

## Plan de trabajo
Para lograr el objetivo deseado se seguirán los siguientes pasos:

1. **ETL:** se comenzará transformado el csv en dataframe para analizarlo y proceder a su limpieza. La limpieza estará orientada a la visualización de los datos y su ingesta en una base de datos relacional sql, de modo que nos centraremos en que sean del tipo correcto, que los strings tengan una tipografía y una nomenclatura unificadas, y eliminaremos las columnas que contenga datos irrelevantes o tan pocos datos que su contenido no nos aporte información útil.
   
2. **Visualización:** con los datos limpios se procederá a realizar una primera visualización de los datos con el objetivo de entender bien la problemática y diseñar una serie de dashboards en Tableau. El proyecto de Tableau se puede ver en [Tableau](https://public.tableau.com/app/profile/miguel.tuda/viz/Empleados_17031734705680/Portada)
  
3. **Base de datos SQL:** finalmente se creará una base de datos relacional SQL y se automatizará la ingesta de los datos limpios a travé de python.

## Estructura del proyecto
El proyecto está organizado del siguiente modo:

* **01_limpieza.ipynb:** contiene la limpieza del csv original y exporta el resultado para operaciones posteriores.
* **02_visualización.ipynb:** primera aproximación a los datos a través de gráficas, orientada a diseñar dashboards en Tableau.
* **03_sql_bbdd.ipynb:** creación de tablas e ingesta de datos a una base de datos sql.
* **data:** directorio que contiene los datos de origen y los que se van generando durante la ETL.
* **empleados_package:** directorio que contiene ficheros .py con funciones que se utilizan a lo largo del proyecto. Son los siguientes:
  * **visualizacion.py:** funciones de visualización adaptadas a las necesidades concretas del proyecto.
  * **outliers.py:** funciones para el tratamiento de outliers.
  *  **sql.py:** funciones para conectarse a un server mysql.
* **images:** imáges generadas durante el desarrollo del proyecto, sobre todo gráficas de visualización de datos.
* **sql:** directorio que contiene el fichero generado al exportar la base de datos creada
  * **empleados.mwb:** resultado de exportar la base de datos recién creada en python.

## Análisis y conclusiones
Ahora comentaremos algunas conclusiones deducidas del análisis y visualización de los datos.

### Análisis
* Parece que la mayor de las fugas se dan entre los más jóvenes, seguidos por los más mayores.

![hist_por_attAge](https://github.com/Origamologo/Empleados/blob/main/images/hist_por_attAge.png)

* La permanencia en la empresa reduce el riesgo de fuga. Quizá sí exista un buen programa de crecimiento laboral, pero no es adecuadamente comunicado a los trabajadores que llevan poco tiempo.

![hist_por_attYears](https://github.com/Origamologo/Empleados/blob/main/images/hist_por_attYears.png)

* Parece que los trabajadores con una categoría laboral (íntimamente relacionada con el sueldo) inferior tienden a abandonar la empresa más. Encaja con los dicho anteriormente, es lógico que los jóvenes entren con una categoría baja y si se marchan, no llegan a escender dentro de la empresa.

![hist_por_jobLevel](https://github.com/Origamologo/Empleados/blob/main/images/hist_por_jobLevel.png)

* Los que se marchan son los que menos y los que más STOCK_OPTION_LEVEL tienen. Esto encaja con os dicho anteriormente respecto a la edad y respecto al sueldo. Los más jóvenes y los más mayores son los que tendrá este valor más alto y más bajo.

![hist_por_attStock](https://github.com/Origamologo/Empleados/blob/main/images/hist_por_attStock.png)

* Sin que BUSINESS_TRAVEL tenga un impacto demasiado fuerte, parece que los que viajan con frecuencia tienen más tendencia a abandonar la empresa.

![quesitos_travel](https://github.com/Origamologo/Empleados/blob/main/images/quesitos_travel.png)

* Los que abandonan la empresa hay más que responden positivamente a OVER_TIME que entre los que se quedan.

![quesitos_overtime](https://github.com/Origamologo/Empleados/blob/main/images/quesitos_overtime.png)

* Entre los que abandonan la empresa hay más que responden positivamente a OVER_TIME que entre los que se quedan.

![quesitos_overtime](https://github.com/Origamologo/Empleados/blob/main/images/quesitos_overtime.png)

* En JOB_ROLE sí que hay un claro ganador, sales_representative es quien presenta mayor índice de abandono, seguido de laboratory_technician.

![hist_por_attRole](https://github.com/Origamologo/Empleados/blob/main/images/hist_por_attRole.png)

* Por último, curiosamente parece que los solteros tienen más tendencia a abandonar la empresa y los divorciado a quedarse, según podemos ver en MARITAL_STATUS.

![quesitos_marital](https://github.com/Origamologo/Empleados/blob/main/images/quesitos_marital.png)

### Conclusiones
Del análisis que acabamos de realizar, podemos trasladar estas conclusiones al departamento de recursos humanos:

*Hay que mejorar la comunicación entre la empresa y sus nuevos empleados, sobre todo los más jóvenes, para que conozcan las posibilidades de desarrollar una carrera laboral larga y exitosa.

*Sería interesante aumentar las categorías laborales en los primeros puestos para que ese salto profesional llegue antes y se perciva mejor el progreso.

*Los senior podrían compartir su experiencia con los recién llegados para que sepan por qué merece la pena quedarse.

*Es importante tratar con especial mimo a los sale representative, quizá aumentarles los beneficios por las acciones, y desde luego vigilar que no se haga un número excesivo de horas extra.

*Sería interesante repartir los viajes de trabajo en la medida de lo posible, y organizar eventos lúdicos que aumenten la felicidad de los trabajadores y, por qué no, reduzcan el número de solteros en plantilla.
