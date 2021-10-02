#!/usr/bin/env python
# coding: utf-8

# In[56]:

# antes de rodar pela primeira vez de instalar o bootstrap pelo comando pip install dash-bootstrap-components

import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
mapa.update_layout(clickmode='event+select')

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='mapa',figure=mapa)
        ]),
        
        dbc.Col([
            dcc.Graph(id='vazoes',figure=vazoes_graph(0)),
            dcc.Graph(id='media_mensal',figure=media_mensal_graph(0)),
            dcc.Graph(id='minmax',figure=minmax_graph(0)),
            dcc.Graph(id='desvio',figure=desvio_media(0)),
            dcc.Graph(id='rosquinha',figure=vazoes_extremas(0)),
            dcc.Graph(id='ciclo_anual',figure=ciclo_anual_graph(0)),
            html.Pre(id='click-data')
        ], xs=8, sm=8, md=8, lg=7, xl=7)
    ])
])

@app.callback(
    Output('click-data', 'children'),
    Input('mapa', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

@app.callback(
    Output('vazoes', 'figure'),
    Input('click-data', 'children'))
def atualizar_vazoes(rio):
    rio = json.loads(rio)
    rio = rio['points'][0]['hovertext'] 
    return vazoes_graph(rio)

@app.callback(
    Output('media_mensal', 'figure'),
    Input('click-data', 'children'))
def atualizar_medias_mensais(rio):
    rio = json.loads(rio)
    rio = rio['points'][0]['hovertext'] - 1  
    return media_mensal_graph(rio)

@app.callback(
    Output('rosquinha', 'figure'),
    Input('click-data', 'children'))
def atualizar_rosquinha(rio):
    rio = json.loads(rio)
    rio = rio['points'][0]['hovertext'] - 1
    return vazoes_extremas(rio)

@app.callback(
    Output('ciclo_anual', 'figure'),
    Input('click-data', 'children'))
def atualizar_ciclo_anual(rio):
    rio = json.loads(rio)
    rio = rio['points'][0]['hovertext'] - 1
    return ciclo_anual_graph(rio)

@app.callback(
    Output('minmax', 'figure'),
    Input('click-data', 'children'))
def atualizar_minmax(rio):
    rio = json.loads(rio)
    rio = rio['points'][0]['hovertext'] - 1
    return minmax_graph(rio)

app.run_server()


# In[ ]:




