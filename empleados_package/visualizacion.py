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



    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Visualizacion de los datos numéricos en un heatmap
def mapa_calor(dataframe, size=(30,20), nombre_fichero="heatmap"):
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
    dataframe.hist(bins = 50, figsize = size)
    save_fig(nombre_fichero)
    plt.show()

# Visualizacion de los datos categóricos en subplots de histogramas
def categoricos(y, x, dataframe, size=(25,35), nombre_fichero="subplots"):
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
    fig, ax = plt.subplots(y, 1, figsize=size)
    columnas = dataframe.select_dtypes(include = "number").columns
    for i in range(len(columnas)):
        sns.boxplot(x=columnas[i], data=dataframe, ax=ax[i])

    plt.tight_layout()
    save_fig(nombre_fichero)
    plt.show()

