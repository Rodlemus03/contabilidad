from operator import truediv
import pandas
from tkinter import messagebox
from tkinter import filedialog as fd
import os



class principal:
    def __init__(self):
    #Variables globales
        self.listaUtiles=[]
        self.menu()
  
    def abrir(self):
        try:
            archivo=fd.askopenfilename(title="Abrir un archivo")
            abierto=open(archivo,'r',encoding='UTF-8')
            self.df=pandas.read_csv(abierto,index_col=False)
            self.bandera=True

        except:
            print("Ocurrio un error")
    def depurar(self):
        titulos=self.df.columns.values
        contador=1
        for i in titulos:
            cadena=""
            cadena+=str(contador)
            cadena+=". "+i
            print(cadena)
            contador+=1
        respuesta="y"
        pos=0

        while respuesta=='y':
            pos=int(input("\n\n\nIngresa el numero de la columna que deseas ----->"))
            if pos>0 and pos<31:
                self.listaUtiles.append(titulos[pos-1])
                respuesta=input("\n\n\nDeseas agregar mas columnas? y/n------>")
            else:
                print("Elige una opcion correcta ")
        self.dfNuevo=self.df[list(set(self.listaUtiles))]
            

    def mostrarDatos(self):
        print(self.dfNuevo)
    def calculos(self):
        pass
    def salir(self):
        print("Feliz dia")
    def menu(self):
        respuesta=0
        #Bandera
        banderaAbrir=False
        banderaDepurar=False
        while(respuesta!=5):
            print("\n\n1. Abrir csv")
            print("2. Depurar")
            print("3. Mostrar datos")
            print("4. Hacer calculos")
            print("5. Salir")
            respuesta=int(input("Selecciona la opcion--->"))
            if respuesta==1:
                self.abrir()
                banderaAbrir=True
            elif respuesta==2:
                if banderaAbrir:
                    self.depurar()
                    banderaDepurar=True
                else:
                    print("Debes de abrir primero")
            elif respuesta==3:
                if banderaAbrir and banderaDepurar:
                    self.mostrarDatos()
                    
                else:
                    print("Debes de abrir primero")
            elif respuesta==4:
                if banderaAbrir:
                    print("Hacer calculos")
                else:
                    print("Debes de abrir primero")
            else:
                print("feliz dia")
principal()