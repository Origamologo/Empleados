import numpy as np

def detectar_outliers(lista_columnas, dataframe): 

    """
    Detecta los outliers en las columnas especificadas de un DataFrame.

    Parámetros:
    - lista_columnas (list): Lista de nombres de columnas en las que se buscarán outliers.
    - dataframe (pandas.DataFrame): El DataFrame que contiene los datos.

    Retorna:
    - dicc_indices (dict): Un diccionario que contiene los índices de los outliers encontrados
      para cada columna especificada. Las claves son los nombres de las columnas y los valores son
      listas de índices.

    Comentarios:
    - Utiliza el método del rango intercuartílico (IQR) para identificar outliers en cada columna.
    - Los outliers se determinan comparando los valores de las columnas con los límites inferior y
      superior calculados a partir de los percentiles 25 y 75.
    - Si no se encuentran outliers en una columna, no se incluye en el diccionario resultante.
    """ 
    
    dicc_indices = {} 
    
    for col in lista_columnas:
        
        Q1 = np.nanpercentile(dataframe[col], 25)
        Q3 = np.nanpercentile(dataframe[col], 75)
        
        IQR = Q3 - Q1
        
        outlier_step = 1.5 * IQR
        
        outliers_data = dataframe[(dataframe[col] < Q1 - outlier_step) | (dataframe[col] > Q3 + outlier_step)]
        
        
        if outliers_data.shape[0] > 0:
        
            dicc_indices[col] = (list(outliers_data.index))
        
    return dicc_indices 


def eliminar_outliers(lista_columnas, dataframe):

    """
    Elimina las filas correspondientes a los outliers en las columnas especificadas de un DataFrame.

    Parámetros:
    - lista_columnas (list): Lista de nombres de columnas en las que se buscarán outliers.
    - dataframe (pandas.DataFrame): El DataFrame que contiene los datos.

    Retorna:
    - final (pandas.DataFrame): Un nuevo DataFrame que excluye las filas correspondientes a los
      outliers en las columnas especificadas.

    Comentarios:
    - Utiliza la función detectar_outliers para identificar los outliers y luego elimina las filas
      correspondientes del DataFrame original.
    - Preserva el DataFrame original y devuelve un nuevo DataFrame sin las filas de outliers.
    """
    
    dict_outliers = detectar_outliers(lista_columnas, dataframe)

    valores = list(dict_outliers.values())
    valores = [indice for sublista in valores for indice in sublista]
    valores = set(valores)

    df_sin_outliers = dataframe.copy()

    final = df_sin_outliers.drop(df_sin_outliers.index[list(valores)] )

    return final