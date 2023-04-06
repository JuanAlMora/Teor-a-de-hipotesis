import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from statistics import stdev,mean
import pandas as pd
import os

def graficarCurvaDeDistribucionNormal(media,desviacion, pValor):
    normal = st.norm(media, desviacion)
    x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
    fp = normal.pdf(x) 
    plt.plot(x, fp)
    plt.title('Distribución Normal')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    c = 'g'
    plt.axvline(media + pValor, label='P Valor: {}'.format(pValor), c=c)
    plt.legend()
    plt.show()

def graficarCurvaDeDistribucionNormalDiferentesDe(media,desviacion, pValor):
    normal = st.norm(media, desviacion)
    x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
    fp = normal.pdf(x) 
    plt.plot(x, fp)
    plt.title('Distribución Normal')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    c = 'g'
    plt.axvline(media + pValor, label='P Valor: {}'.format(pValor), c=c)
    plt.axvline(media - pValor, label='P Valor: {}'.format(-pValor), c=c)
    plt.legend()
    plt.show()

def graficarResultadoDiferenteDe(media,desviacion, pValor, z):
    normal = st.norm(media, desviacion)
    x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
    fp = normal.pdf(x) 
    plt.plot(x, fp)
    plt.title('Distribución Normal')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    c = 'r'
    plt.axvline(media + pValor, label='P Valor: {}'.format(pValor), c=c)
    plt.axvline(media - pValor, label='P Valor: {}'.format(- pValor), c=c)
    c = 'g'
    plt.axvline(media + z, label='Z: {}'.format(z), c=c)
    plt.legend()
    plt.show()


def graficarResultado(media,desviacion, pValor, z):
    normal = st.norm(media, desviacion)
    x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
    fp = normal.pdf(x) 
    plt.plot(x, fp)
    plt.title('Distribución Normal')
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    c = 'r'
    plt.axvline(media + pValor, label='P Valor: {}'.format(pValor), c=c)
    c = 'g'
    plt.axvline(media + z, label='Z: {}'.format(z), c=c)
    plt.legend()
    plt.show()

def mostrarContenido(archivos):
    j = 1
    print("\n\n     Elija el archivo a procesar: \n")
    for i in archivos:
        print( "     ", j , ". ", i)
        j += 1

def columnaATrabajar(df):
    print("\n\n     Elija la columna en la que quiere trabajar: \n")
    columna = []
    j = 1
    for i in df:
        columna.append(i)
        print("     ", j, ". ", i)
        j+=1

    res = int(input())
    os.system("cls")
    return columna[res-1]


def respectoExcel():
    pwd = os.getcwd() + '/Datos' 
    contenido = os.listdir(pwd)
    mostrarContenido(contenido)
    archivo = int (input())
    os.system("cls")
    datos = pd.read_csv(pwd + "/" + contenido[archivo-1])
    df = pd.DataFrame(datos)
    columna = columnaATrabajar(df)

    promedio = df[columna].mean()
    desviacion = df[columna].std()
    filas = df.shape[0]
    calculo(desviacion, promedio, filas)

def calculo(desviacion, promedio, ndatos):
    hNula =float( input("\n\n       Ingrese la hipotesis nula: "))
    print("        Elija la hipotesis alternativa: \n")
    print("       1. H1 < ", hNula, "\n       2. H1 != ", hNula, "\n       3. H1 > ", hNula)
    ele = int(input())
    pError = int(input("       Ingrese el porcentaje de error: "))
    if ele == 1:
        menorque(desviacion, promedio, ndatos, pError,hNula)
    elif ele == 2:
        diferentede(desviacion, promedio, ndatos, pError,hNula)
    elif ele == 3:
        mayorque(desviacion, promedio, ndatos, pError,hNula)

def menorque(desviacion, promedio, ndatos, pError,hNula):
    pValor = st.norm.ppf(pError/100)
    graficarCurvaDeDistribucionNormal(promedio,desviacion, pValor)
    z = (promedio - hNula)/(desviacion/(ndatos**(1/2)))
    if z < pValor:
        print("La hipotesis nula es rechazada.")
    else:
        print("La hipotesis nula es aceptada.")
    
    graficarResultado(promedio,desviacion, pValor, z)

def diferentede(desviacion, promedio, ndatos, pError,hNula):
    pValor = st.norm.ppf((pError/2)/100)
    graficarCurvaDeDistribucionNormalDiferentesDe(promedio,desviacion, pValor)
    z = (promedio - hNula)/(desviacion/(ndatos**(1/2)))
    if z > pValor and z < -pValor:
        print("La hipotesis nula es aceptada.")
    else:
        print("La hipotesis nula es rechazada.")
    
    graficarResultadoDiferenteDe(promedio,desviacion, pValor, z)

def mayorque(desviacion, promedio, ndatos, pError,hNula):
    pValor = st.norm.ppf((100 - pError)/100)
    graficarCurvaDeDistribucionNormal(promedio,desviacion, pValor)
    z = (promedio - hNula)/(desviacion/(ndatos**(1/2)))
    if z > pValor:
        print("La hipotesis nula es rechazada.")
    else:
        print("La hipotesis nula es aceptada.")
    
    graficarResultado(promedio,desviacion, pValor, z)

def respectoMedia():
    ndatos = int(input("Ingrese la cantidad de datos tomados: "))
    promedio = float(input("Ingrese la media de los datos: "))
    desviacion = float(input("Ingrese la desviacion estandar: "))
    calculo(desviacion, promedio, ndatos)  

def menu():
    while(True):
        os.system("cls")
        print("\n\n     Menu Principal: \n")
        print("""\n     1. Teoria de hipotesis respecto a tabla de excel.\n     2. Teroia de hipotesis respecto a media.\n     0. Salir""")
        
        ele = int(input())
        os.system("cls")
        if ele == 1:
            respectoExcel()
        elif ele == 2:
            respectoMedia()
        else:
            break
    
    # print(st.norm.ppf(0.05))

menu()