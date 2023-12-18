import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Función para guardar las imágenes que se vayan generando
PROJECT_ROOT_DIR = "."
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images")
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=100):

    """
    Guarda una imagen en un archivo con opciones de formato y resolución especificadas.

    Parámetros:
    - fig_id (str): Identificador único para la imagen.
    - tight_layout (bool): Controla si se aplica un diseño ajustado a la imagen.
    - fig_extension (str): Extensión del archivo de la imagen (por ejemplo, "png", "jpg").
    - resolution (int): Resolución de la imagen en puntos por pulgada (dpi).

    Retorna:
    - None: Guarda la imagen en un archivo con el nombre y formato especificados.

    Comentarios:
    - La función utiliza Matplotlib para guardar la imagen en un archivo en el directorio 'images'.
    - 'fig_id' se utiliza para generar el nombre del archivo.
    - 'tight_layout' controla si se aplica un diseño ajustado antes de guardar la imagen.
    """

    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Visualizacion de los datos numéricos en un heatmap
def mapa_calor(dataframe, size=(30,20), nombre_fichero="heatmap"):

    """
    Crea un mapa de calor para visualizar las correlaciones entre variables numéricas en un DataFrame.

    Parámetros:
    - dataframe (pd.DataFrame): DataFrame que contiene los datos.
    - size (tuple): Tamaño de la imagen (ancho, alto).
    - nombre_fichero (str): Nombre del archivo para guardar la imagen.

    Retorna:
    - None: Muestra y guarda la grafica.

    Comentarios:
    - La función utiliza Seaborn y Matplotlib para crear un mapa de calor de las correlaciones entre columnas numéricas.
    - El mapa de calor utiliza colores para representar las fuerzas y direcciones de las correlaciones.
    """

    mask = np.triu(np.ones_like(dataframe.select_dtypes(include='number').corr(), dtype = bool))
    plt.figure(figsize=size)
    sns.heatmap(dataframe.select_dtypes(include='number').corr(), 
            cmap = "YlGnBu", 
                mask = mask,
            annot = True)
    save_fig(nombre_fichero)
    plt.show();

# Visualizacion de los datos numéricos en un histograma
def histograma(dataframe, size=(20,15), nombre_fichero="histogram"):

    """
    Crea un histograma para visualizar la distribución de variables numéricas en un DataFrame.

    Parámetros:
    - dataframe (pd.DataFrame): DataFrame que contiene los datos.
    - size (tuple): Tamaño de la imagen (ancho, alto).
    - nombre_fichero (str): Nombre del archivo para guardar la imagen.

    Retorna:
    - None: Muestra y guarda la grafica.

    Comentarios:
    - La función utiliza la función 'hist' de Pandas para generar histogramas de las columnas numéricas.
    """

    dataframe.hist(bins = 50, figsize = size)
    save_fig(nombre_fichero)
    plt.show()

# Visualizacion de los datos categóricos en subplots de histogramas
def categoricos(y, x, dataframe, size=(25,35), nombre_fichero="subplots"):

    """
    Crea subgráficos de barras horizontales para visualizar la distribución de variables categóricas en un DataFrame.

    Parámetros:
    - y (int): Número de filas de subgráficos.
    - x (int): Número de columnas de subgráficos.
    - dataframe (pd.DataFrame): DataFrame que contiene los datos.
    - size (tuple): Tamaño de la imagen (ancho, alto).
    - nombre_fichero (str): Nombre del archivo para guardar la imagen.

    Retorna:
    - None: Muestra y guarda la grafica.

    Comentarios:
    - Cada subgráfico representa la distribución de una columna categórica en el DataFrame.
    - La función utiliza gráficos de barras horizontales para visualizar las frecuencias de categorías.
    """

    fig, axes = plt.subplots(y, x, figsize = size)

    axes = axes.flat

    columnas_object = dataframe.select_dtypes(include = "object").columns

    for i, colum in enumerate(columnas_object):
        dataframe[colum].value_counts().plot.barh(ax = axes[i])
        axes[i].set_title(colum, fontsize = 20, fontweight = "bold")
        axes[i].tick_params(labelsize = 20)
        axes[i].set_xlabel("")

    save_fig(nombre_fichero)  
    fig.tight_layout();

# Boxplot
def boxplot(y, dataframe, size=(25,35), nombre_fichero="boxplot"):

    """
    Crea subgráficos de tipo boxplot para visualizar la distribución de variables numéricas en un DataFrame.

    Parámetros:
    - y (int): Número de subgráficos en la columna.
    - dataframe (pd.DataFrame): DataFrame que contiene los datos.
    - size (tuple): Tamaño de la imagen (ancho, alto).
    - nombre_fichero (str): Nombre del archivo para guardar la imagen.

    Retorna:
    - None: Muestra y guarda la grafica.

    Comentarios:
    - La función utiliza Seaborn para crear boxplots.
    - Cada subgráfico representa la distribución de una columna numérica en el DataFrame.
    """

    fig, ax = plt.subplots(y, 1, figsize=size)
    columnas = dataframe.select_dtypes(include = "number").columns
    for i in range(len(columnas)):
        sns.boxplot(x=columnas[i], data=dataframe, ax=ax[i])

    plt.tight_layout()
    save_fig(nombre_fichero)
    plt.show()
