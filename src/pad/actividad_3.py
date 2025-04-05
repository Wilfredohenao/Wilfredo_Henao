
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
            "detalle":["Crea un DataFrame frutas que luzca así","Crea un DataFrame ventas_frutas que coincida con el diagrama","Crea una variable utensilios con una Serie que tenga el siguiente aspecto:","Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura.","Visualiza las primeras filas del DataFrame","","","","","","",""],
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
            name="Cocina", dtype= "object")
        df_3.to_csv(r"/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_3.csv")
        self.df.loc[2,"resultado"] = "/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_3.csv"
        print("punto_3")
    def punto_4(self):
      ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
      df_4 = pd.read_csv(ruta_winemag)
      df_4 = df_4.head()
      df_4 = df_4.tail()
      df_4.to_csv(r"/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_4.csv")   
      self.df.loc[3,"resultado"] = "/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_4.csv"        
    print("punto_4") 
    def punto_5(self):
        ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df_5 = pd.read_csv(ruta_winemag)
        df_5 = df_5.head()
        df_5.to_csv(r"/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_5.csv")
        self.df.loc[4,"resultado"] = "/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_5.csv"
        print("punto_5") 
       
    def punto_6(self):
        df = pd.read_csv(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df_6 = df.info()
        df_6.to_csv(r"/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_6.csv")
        self.df.loc[5,"resultado"] = "/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_6.csv"
        print("punto_6") 
    def punto_7(self):
        df_7= pd.DataFrame()
        ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df = pd.read_csv()
        df_7 = df.mean()
        df_7.to_csv(r"/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_7.csv")
        self.df.loc[5,"resultado"] = "/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_7.csv"
        print("punto_7") 
    def punto_8(self):
        df_8 = pd.DataFrame()
        precio_maximo = df['precio'].max()
        print(precio_maximo)
        ruta_winemag = os.path.join(self.ruta_act2, "winemag-data_first150k.csv.zip")
        df = pd.read_csv()  
        df_8.to_csv("/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_8.csv")
        self.df.loc[7,"resultado"] = "/workspaces/Wilfredo_Henao/src/pad/actividad_3/punto_8.csv"
        print("punto_8") 
    def punto_9(self):
        self.df.loc[8,"resultado"] = len(self.df)+8
        print("punto_9") 
    def punto_10(self):
        
        self.df.loc[9,"resultado"] = len(self.df)+9
        print("punto_10") 
    def punto_11(self):
        self.df.loc[10,"resultado"] = len(self.df)+10
        print("punto_11") 
    def punto_12(self,num=100):
        self.df.loc[11,"resultado"] = len(self.df)+11
        print("punto_12") 
    
    def ejecutar(self):
      self.punto_1()     
      self.punto_2() 
      #self.punto_3() 
      #self.punto_4() 
      #self.punto_5() 
     #self.punto_6() 
     #self.punto_7() 
     #self.punto_8() 
      #  self.punto_9() 
      #  self.punto_10()
      #  self.punto_11()
      #  self.punto_12()
       # self.df.to_csv("actividad3.csv")

    
      self.df.to_csv("actividad3.csv", index=False)
    print("Datos guardados en actividad3.csv")
        
act = actividad3()
act.ejecutar()
