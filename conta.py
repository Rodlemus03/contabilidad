import pandas
from tkinter import messagebox
from tkinter import filedialog as fd



class principal:
    def __init__(self):
    #Variables globales
        self.menu()
  
    def abrir(self):
        archivo=fd.askopenfilename(title="Abrir un archivo")
        abierto=open(archivo,'r',encoding='UTF-8')
        self.df=pandas.read_csv(abierto,index_col=False)
        listaUtiles=['Fecha de emisi�n','N�mero de Autorizaci�n','Tipo de DTE (nombre)','Serie','N�mero del DTE']
        print(self.df[listaUtiles])
    def depurar(self):
        pass
    def mostrarDatos(self):
        pass
    def calculos(self):
        pass
    def salir(self):
        print("Feliz dia")
    def menu(self):
        respuesta=0
        #Bandera
        banderaAbrir=False
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
                    print("depurar")
                else:
                    print("Debes de abrir primero")
            elif respuesta==3:
                if banderaAbrir:
                    print("Mostrar datos")
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