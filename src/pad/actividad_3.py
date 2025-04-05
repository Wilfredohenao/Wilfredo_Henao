
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import os
# import kagglehub  # Uncomment this line if you install kagglehub and need it
import os
import requests
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad3:
    def __init__(self):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/pad/actividad_3/".format(self.ruta_raiz)
        datos = {
            "n_punto": [1,2,3,4,5,6,7,8,9,10,11,12],
            "detalle":["Crea un DataFrame frutas que luzca así","Crea un DataFrame ventas_frutas que coincida con el diagrama","Crea una variable utensilios con una Serie que tenga el siguiente aspecto:","Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura.","Visualiza las primeras filas del DataFrame","Utiliza el método .info() para averiguar cuántas entradas hay. ¿Cuántas encontraste?","¿Cuál es el precio promedio?","¿Cuál es el precio más alto pagado?","Crea un DataFrame con todos los vinos de california","Utiliza idxmax() para encontrar el índice del vino con el precio más alto y luego utiliza loc para obtener toda la información de ese vino específico","",""],
            "resultado":[0,0,0,0,0,0,0,0,0,0,0,0],
            
        }
        self.df = pd.DataFrame(datos)
        print(self.ruta_raiz)  
    def punto_1(self):
        df_1 = pd.DataFrame({
            "granadilla": [20],
            "tomates": [50],
        })
        df_1.to_csv(r"src/pad/actividad_3/punto_1.csv")
        self.df.loc[0,"resultado"] = "src/pad/actividad_3/punto_1.csv"
        print("punto_1")

    def punto_2(self):
        df_2 = pd.DataFrame(
            {"Granadilla": [20, 49], "Tomates": [50, 100]},
            index=["ventas 2021", "ventas 2022"]
        )
        df_2.to_csv(r"src/pad/actividad_3/punto_2.csv")
        self.df.loc[1,"resultado"] = "src/pad/actividad_3/punto_2.csv"
        print("punto_2")
    def punto_3(self): 
        df_3 = pd.Series(
            data=["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
            index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
            name="Cocina", dtype= "object"
        )
        df_3.to_csv(r"src/pad/actividad_3/punto_3.csv")
        self.df.loc[2,"resultado"] = "src/pad/actividad_3/punto_3.csv"
        print("punto_3")
    def punto_4(self):
        ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df_4 = pd.read_csv(ruta_winemag)
        df_4 = df_4.head()
        df_4.to_csv(r"src/pad/actividad_3/punto_4.csv")   
        self.df.loc[3,"resultado"] = "src/pad/actividad_3/punto_4.csv"        
        print("punto_4") 
    def punto_5(self):
        ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df_5 = pd.read_csv(ruta_winemag)
        df_5 = df_5.head()
        df_5.to_csv(r"src/pad/actividad_3/punto_5.csv")
        self.df.loc[4,"resultado"] = "src/pad/actividad_3/punto_5.csv"
        print("punto_5")     
    def punto_6(self):
        ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df_6 = pd.read_csv(ruta_winemag)
        df_6.info()
        print(df_6.info())
        df_6.to_csv(r"src/pad/actividad_3/punto_6.csv")
        self.df.loc[5,"resultado"] = "src/pad/actividad_3/punto_6.csv"
        print("punto_6") 
    def punto_7(self):
        ruta_winemag = os.path.join (self.ruta_act2 , "winemag-data_first150k.csv.zip")
        df_7 = pd.read_csv(ruta_winemag)
        df_7['price'].mean()
        df_7.to_csv(r"src/pad/actividad_3/punto_7.csv")
        self.df.loc[6,"resultado"] = "src/pad/actividad_3/punto_7.csv"
        print("punto_7") 
    def punto_8(self):
        ruta_winemag = os.path.join (self.ruta_act2  , "winemag-data_first150k.csv.zip")
        df_8 = pd.read_csv(ruta_winemag)
        df_8 ['price'].max()
        df_8.to_csv(r"src/pad/actividad_3/punto_8.csv")
        self.df.loc[7,"resultado"] = "src/pad/actividad_3/punto_8.csv"
        print("punto_8") 
    def punto_9(self):
        ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df_9 = pd.read_csv(ruta_winemag)
        df_california = df_9[df_9['province']=="California"]
        df_california.to_csv(r"src/pad/actividad_3/punto_9.csv")
        df_california = df_california.head() 
        df_california["description"] = df_california["description"].str.slice(0, 20) + "..."
        df_california["variety"] = df_california["variety"].str.slice(0, 10) + "..."
        df_california["designation"] = df_california["designation"].astype(str).str.slice(0, 10) + "..." 
        self.df.loc[8,"resultado"] = "src/pad/actividad_3/punto_9.csv"        
        print("punto_9") 
    def punto_10(self):
        df_10 = pd.read_csv("src/pad/actividad_3/punto_9.csv")
        df_california = df_10[df_10['province'] == "California"]
        df_california.to_csv(r"src/pad/actividad_3/punto_10.csv")
        idx_mas_caro = df_california['price'].idxmax()
        vino_mas_caro = df_california.loc[idx_mas_caro]
        self.df.loc[9, "resultado"] = "src/pad/actividad_3/punto_10.csv" 
        print("punto_10") 
        print("El vino más caro de California es:")
        print(vino_mas_caro.to_string()) 
    def punto_11(self):
        ruta_winemag = os.path.join(self.ruta_act2 , "winemag-data_first150k.csv.zip")
        df_11 = pd.read_csv(ruta_winemag)
        df_ca = df_11[df_11['province'] == 'California']
        varieties = df_ca['variety'].value_counts()
        print(varieties.head(5))
        df_11.to_csv(r"src/pad/actividad_3/punto_11.csv")
        self.df.loc[10,"resultado"] = "src/pad/actividad_3/punto_11.csv"
        print("punto_11")
        
    def punto_12(self,num=100):
        ruta_winemag = os.path.join(self.ruta_act2 , "winemag-data_first150k.csv.zip")
        df_12 = pd.read_csv(ruta_winemag)
        df_ca = df_12[df_12['province'] == 'California']
        variety_counts = df_ca['variety'].value_counts()
        top_10_varieties = variety_counts.head(10)
        df_12.to_csv(r"src/pad/actividad_3/punto_12.csv")
        self.df.loc[11,"resultado"] = "src/pad/actividad_3/punto_12.csv"
        print(top_10_varieties)
    
    def ejecutar(self):
      self.punto_1()     
      self.punto_2() 
      self.punto_3() 
      self.punto_4() 
      self.punto_5() 
      self.punto_6() 
      self.punto_7() 
      self.punto_8() 
      self.punto_9() 
      self.punto_10()
      self.punto_11()
      self.punto_12()
      self.df.to_csv("actividad3.csv")

    
      self.df.to_csv("actividad3.csv", index=False)
    print("Datos guardados en actividad3.csv")
        
act = actividad3()
act.ejecutar()
