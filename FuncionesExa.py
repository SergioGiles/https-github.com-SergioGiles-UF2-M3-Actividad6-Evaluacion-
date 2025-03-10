import pandas as pd
import numpy as np

def cargar_archivo(file_path):
    
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Este formato no está soportado para esta función: {file_path.split('.')[-1]}")

def reemplazar_nulos(df):
    
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            if df.columns.get_loc(col) % 2 == 0:
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(99, inplace=True)
        else:
            df[col].fillna("Este_es_un_valor_nulo", inplace=True)
    return df

def detectar_nulos(df):
    
    nulos_por_columna = df.isnull().sum()
    total_nulos = df.isnull().sum().sum()
    return nulos_por_columna, total_nulos

def reemplazar_atipicos(df):
    
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        df[col] = np.where((df[col] < limite_inferior) | (df[col] > limite_superior), df[col].median(), df[col])
    return df
