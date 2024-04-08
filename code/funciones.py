import pandas as pd # type: ignore

def leer_datos(archivo, columna):
    """
    Esta función lee un csv y convierte la columna TS en formato datetime.
    
    Argumentos:
    archivo: Nombre del archivo csv.
    columna: Nombre de la columna con fecha
    
    Returns:
    Un DataFrame con la columna de fecha convertida en formato datetime
    """
    df = pd.read_csv(archivo)
    df[columna] = pd.to_datetime(df[columna])
    return df



def filtrar_calcular_media(df,column_name, nombre):
    """
    Esta función filtra los datos de la columna Tag para un nombre determinado usando formato "Examen_NOMBRE_ALUMNO" 
    y calculará el promedio
    
    Argumentos:
    df: DataFrame con datos
    nombre: Nombre que se desea filtrar
    
    Returns:
    Un DataFrame aplicando un filtro a la columna Tag visualizando un nombre en especifico y su media
    """
    data_alumno = df[df[column_name] == 'Examen_' + nombre]
    media = data_alumno['Value'].mean()
    return media