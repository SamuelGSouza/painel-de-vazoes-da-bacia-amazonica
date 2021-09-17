import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go

Q = pd.read_csv('MGB-IPH_DischargeData_AmazonBasin.txt', delimiter="\s+",engine='python',header=None)
ti='1998-01-01'
tf='2009-12-31'
date = pd.date_range(start=ti, end=tf, freq='D')
Q['date'] = date
Q.set_index('date', inplace=True)

np_array = Q.to_numpy() # transforma o DataFrame em um array
valor_min =np_array[0][0] # inicializa a variável que armazenará o valor mínimo
valor_max = 0 # inicializa a variável que armazenará o valor máximo
list_max = [] # inicializa o array que contém os valores máximos 
list_min = [] # inicializa o array que contém os valores mínimos
dias = 0 # inicializa a variável que recebe o valor de dias
ano = [x+1 for x in range(1997,2009)] # cria um array que contém todos os anos de 1998 até 2009

for j in range(12): # for para cada ano a ser analizado
    for i in range(365): # for que percorre todos os dias em um ano de um rio da matriz
        if np_array[i+dias][0]> valor_max: # verifica se o valor atual é maior que o valor anterior
            valor_max = np_array[i+dias][0] # atualiza o valor máximo se o atual for maior que o anterior
        if np_array[i+dias][0] < valor_min: # verifica se o valor atual é menor que o valor anterior
            valor_min = np_array[i+dias][0] # atualiza o valor mínimo se o atual for menor que o anterior
    list_max.append(valor_max) # adicona o valor máximo dentro da lista de valores máximos
    list_min.append(valor_min) # adicona o valor mínimo dentro da lista de valores mpinimos
    valor_min =np_array[1][0] # limpa a variável de valores mínimos para ir para o próximo ano
    valor_max = 0 # limpa a variável de valores máximos para ir para o próximo ano
    if ano[j]%4==0: # verifica se o ano é bissexto
        dias += 366 # atualiza o valor dos dias se o ano for bissexto
    else:
        dias += 365 # atualiza o valor dos dias se o ano for normal


fig = go.Figure(data=[ # plota o gráfico 
    go.Bar(name='Max', x=ano, y=list_max, marker_color='rgb(55, 83, 109)'),
    go.Bar(name='Min', x=ano, y=list_min, marker_color='rgb(26, 118, 255)')
])
# Muda o modo da barra
fig.update_layout(barmode='group')

fig.update_layout(
    title='Vazão Mínima e Máxima Anual ',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Vazão (m³/s)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # espaço entre barras de coordenadas de localização adjacentes.
    bargroupgap=0.1 # espaço entre as barras da mesma coordenada de localização.
)

fig.show()
