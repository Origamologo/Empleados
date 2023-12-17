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
def mapa_calor(dataframe, nombre_fichero="heatmap"):
    mask = np.triu(np.ones_like(dataframe.select_dtypes(include='number').corr(), dtype = bool))
    plt.figure(figsize=(30,20))
    sns.heatmap(dataframe.select_dtypes(include='number').corr(), 
            cmap = "YlGnBu", 
                mask = mask,
            annot = True)
    save_fig(nombre_fichero)
    plt.show();