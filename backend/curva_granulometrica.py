import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import io
import base64
import numpy as np

#valores de entrada
nombre = [
    "No. 4",
    "No. 10",
    "No. 20",
    "No. 40",
    "No. 60",
    "No. 140",
    "No. 200",
    "fondo"
    ]




def curvaGranulometrica(pasa):

    # Definir los datos de entrada y realizar la interpolación
    abertura = [0.075, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    plt.figure(figsize=(14, 4)) 

    plt.plot(abertura,pasa,linestyle='-', marker='o', color='k', fillstyle='none',label='Data') 


    # #Grafica
    plt.title("",fontsize=10)
    plt.xlabel('Diámetro (mm)')
    plt.ylabel('Porcentaje pasa acumulado (%)')
    plt.title('Curva granulométrica')
    plt.legend() 
    plt.xscale("log")
    plt.xlim(0.075,4.75)
    plt.ylim(0,100) 
    plt.grid(color='k',lw='0.1',ls='-')
    
    # # #se agregan más grillas
    ax1 = plt.gca()
    ax1.invert_xaxis()

    # # # Agregar el segundo eje x para los nombres de los tamices
    ax2 = ax1.twiny()
    ax2.set_xscale('log')
    ax2.set_xticks(abertura)
    ax2.set_xticklabels(nombre, rotation=90, fontsize=8)

    # # # Agregar linas de los tamices
    ax2.set_xlabel('Tamices')
    ax2.set_xlim(0.075,4.75)
    ax2.invert_xaxis()

    # # # #agregamos nombre lineas verticales
    L_No10 = ([4.75,4.75]) 
    L_No20 = ([2,2]) 
    L_No40 = ([0.850,0.850]) 
    L_No60 = ([0.425,0.425])
    L_No140 = ([0.106,0.106])  
    L_rango = ([0,100])

    # #se indicca en el plot la ubicación de estas líneas
    plt.plot(L_No10, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No20, L_rango, color='grey', lw='0.8', ls='--') 
    plt.plot(L_No40, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No60, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No140, L_rango, color='grey', lw='0.8', ls='--')

    # # #se agrega textos
    plt.text(4.75, 2, 'Grava(Fina)', fontsize=8, rotation=90)
    plt.text(1.95, 2, 'Arena(Gruesa)', fontsize=8, rotation=90)
    plt.text(0.415, 2, 'Arena(Mediana)', fontsize=8, rotation=90)
    plt.text(0.075, 2, 'Arena(Fina)', fontsize=8, rotation=90)

    x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
    for x in x_values:
        plt.axvline(x=x, color='grey', ls='-', lw='0.3')


    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return image_base64


