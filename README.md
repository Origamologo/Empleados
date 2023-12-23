# Empleados

![portada](https://github.com/Origamologo/Empleados/blob/main/images/portada.jpg)

## Descripción
Este trabajo es la prueba técnica dentro del proceso de selección de profesores de Adalab.\
La idea es desarrollar un proceso completo de ETL sobre un conjunto de datos acerca de los trabajadores de una empresa, divididos entre los que está satisfechos con su tradajo y los que abandonaron para irse a trabajar a otro sitio. En los datos encontraremos los motivos que llevan a unos  a quedarse y a otros a marcharse.

## Objetivo
El objetivo de este trabajo es ser el mejor de los candidatos y conseguir la plaza de profesor en Adalab.\
Para lograrlo se hará una lipieza y tratamiento exahustivo de los datos con dos objetivos:

* Realizar un análisis de los datos que nos permita dilucidar las causas de la fuga de talentos y nos permite proponer una estrategia al departamente de recursos humanos.

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

## Conclusiones
Ahora comentaremos algunas conclusiones deducidas del análisis y visualización de los datos.

* Parece que la mayor de las fugas se dan entre los más jóvenes, seguidos por los más mayores.

![hist_por_attAge](https://github.com/Origamologo/Empleados/blob/main/images/hist_por_attAge.png)

* La permanencia en la empresa reduce el riesgo de fuga. Quizá sí exista un buen programa de crecimiento laboral, pero no es adecuadamente comunicado alas trabajadores que llevan poco tiempo.

