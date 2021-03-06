# WB_EPTA
#Weight and Ballance analysis software fot OpenRocket data (may also work with other rocket simulators)
import csv
import matplotlib.pyplot as plt
import numpy as np

def grupo(i):   # Função para separar as colunas
    list = []
    for row in Info:
        list.append(row[i])
    data.seek(0)  # volta ao início do arquivo
    list = numbers(list)
    return list

def numbers(lista):  # Transformando todos os valores em numeros
    number_list = [0 if x == 'NaN' else float(x) for x in lista]  # recria a lista apenas com floats e elimina os NaN
    return number_list

def filtra(lista):  # Retira os valores após o Apogeu

        nova_lista = lista[:apogeu]
        return nova_lista

def envelope(diametro):  # Gráfico com o envelope em tempo real ( Em mm )
    lim_max_CP = []
    lim_min_CP = []

    for CG in dataCG:
        lim_max_CP.append(CG + (static_margin_max * diametro)) # limite posterior do CP
        lim_min_CP.append(CG + (static_margin_min * diametro))  # Limie anterior do CP

    plt.figure('Envelope')
    plt.plot(time,lim_max_CP,'b', linewidth=0.5,label = 'Limite posterior do CP')
    plt.plot(time,lim_min_CP,'b', linewidth=0.5,label = 'Limite anterior do CP')
    plt.plot(time,dataCP, linewidth=0.5,label = 'Posição do CP')
    plt.legend()
    plt.axis([0,max(time),650,900])
    plt.grid(color='r', linestyle='-', linewidth=0.1)
    plt.title('Envelope de voo')
    plt.xlabel('Tempo [s]')
    plt.ylabel('Distância do nariz [mm]')




    return

def static_margin_plot(diameto):  # Gráfico com a márgem estática apenas

    lim_posterior = [static_margin_max for x in range(len(time))]
    lim_anterior = [static_margin_min for x in range(len(time))]

    plt.figure('Margem Estática ')
    plt.plot(time,lim_posterior, linewidth=0.5,label = 'Margem máxima')
    plt.plot(time,lim_anterior, linewidth=0.5,label = 'Margem mínima')
    plt.plot(time,static_margin, linewidth=0.5,label = 'Margem real')
    plt.legend()

    plt.title('Margem estática')
    plt.xlabel('Tempo [s]')
    plt.ylabel('Margem Estácita [Diâmetro Max.]')


    plt.grid(color='r', linestyle='-', linewidth=0.1)

    return

# Abrindo o arquivo CSV
with open('data.csv') as data:
    Info = csv.reader(data,delimiter = ',')  # transforma cada linha em uma lista (retorna um iterador)


    # Definindo cada variável  (Modificar à medida que for necessário para o projeto)

    rocket_diammeter = 85 # Em milimetros
    static_margin_min = 1  # Em unidades de diâmetro máximo
    static_margin_max = 1.5  # Em unidades de diâmetro máximo

    # Definindo o limite da coleta de dados

    altitude = grupo(1)
    apogeu = altitude.index(max(altitude))  # Dados após o apogeu são inúteis

    # Listas de Dados da simulação
    dataCG = filtra(grupo(4))
    dataCP = filtra(grupo(3))
    time = filtra(grupo(0))
    velocity = filtra(grupo(1))
    static_margin = filtra(grupo(5))

    # Plots de gráficos
    envelope(rocket_diammeter)
    static_margin_plot(rocket_diammeter)
    plt.show()

