
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import os
#import kagglehub
import os
import requests
import zipfile
class actividad3:
    def __init__(self):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act3 = "{}/src/pad/actividad_3f/".format(self.ruta_raiz)
        datos = {
             
            "n_punto": [1,2,3,4,5,6,7,8,9,10,11,12],
            "detalle":["Crea un DataFrame frutas que luzca así","","","","","","","","","","",""],
            "resultado":[0,0,0,0,0,0,0,0,0,0,0,0],
            
        }
        self.df = pd.DataFrame(datos)
        print(self.ruta_raiz)
        self.df = pd.DataFrame(datos)
        print(self.ruta_raiz)
        def punto_1(self):
            df_1 = pd.DataFrame({
                "granadilla": [20],
                "tomates": [50],
            })
            self.df.loc[0, "resultado"] = len(self.df) + 0
            df_1.to_csv(r"/workspaces/Wilfredo_Henao/src/pad/actividad_3f/punto_1.csv")
            self.df.loc[0, "resultado"] = "/workspaces/Wilfredo_Henao/src/pad/actividad_3f/punto_1.csv"
            df_rrss = pd.read_csv(r"/workspaces/Wilfredo_Henao/src/pad/actividad_3f/punto_1.csv")
            print("punto_1")