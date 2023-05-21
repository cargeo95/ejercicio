from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd

import pprint

product_data = {
    "tamiz": ["Num_4", "Num_8", "Num_10", "Num_20", "Num_40", "Num_100", "Num_200", "FONDO", "LIMITE LIQUIDO", "INDICE DE PLASTICIDAD"],
}

df_product = pd.DataFrame(product_data)


#importamos backend
from backend.cartaplasticidad import cartaPlasticidad
from backend.curva_granulometrica import curvaGranulometrica


app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Input(
            id='editing-columns-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='editing-columns-button', n_clicks=0)
    ], style={'height': 50}),

    dash_table.DataTable(
        id='editing-columns',
        columns=[{
            'name': 'Column {}'.format(i),
            'id': 'column-{}'.format(i),
            'deletable': True,
            'renamable': True
        } for i in range(0, 5)],
        data=df_product.to_dict("records"),
        editable=True,
    )
    ,

    html.Div(id='editing-prune-data-output'),
    html.Hr(),
    html.Hr(),
    html.Hr(),
    
    html.Div(id='curva_granulometrica'),
    
])


@app.callback(
    Output('editing-columns', 'columns'),
    Input('editing-columns-button', 'n_clicks'),
    State('editing-columns-name', 'value'),
    State('editing-columns', 'columns'))
def update_columns(n_clicks, value, existing_columns):
    if n_clicks > 0:
        existing_columns.append({
            'id': value, 'name': value,
            'renamable': True, 'deletable': True,
            # 'presentation': 'input'
        })
    return existing_columns


@app.callback(Output('editing-prune-data-output', 'children'),
              Input('editing-columns', 'data'))
def display_output(columns):
    pruned_column_0 = []
    pruned_column_1 = []
    pruned_column_2 = []

    
    for row in columns:
        # Verificar si la columna no está vacía
        if row.get(0) != '':
            pruned_column_0.append(row.get('column-0'))
            pruned_column_1.append(row.get('column-1'))
            pruned_column_2.append(row.get('column-2'))

    
    limite_liquido = []
    Indice_plasticidad = []
    
    if len(pruned_column_0) >= 9:
        limite_0 = pruned_column_0[8]
        indice_0 = pruned_column_0[9]
        
        if limite_0 is not None and limite_0 != 'None':
            limite_0 = int(limite_0.strip("'"))
            limite_liquido.append(limite_0)

        if indice_0 is not None and indice_0 != 'None':
            indice_0 = int(indice_0.strip("'"))
            Indice_plasticidad.append(indice_0)
            
    if len(pruned_column_1) >= 9:
        limite_1 = pruned_column_1[8]
        indice_1 = pruned_column_1[9]
        
        if limite_1 is not None and limite_1 != 'None':
            limite_1 = int(limite_1.strip("'"))
            limite_liquido.append(limite_1)

        if indice_1 is not None and indice_1 != 'None':
            indice_1 = int(indice_1.strip("'"))
            Indice_plasticidad.append(indice_1)
    
    if len(pruned_column_2) >= 9:
        limite_2 = pruned_column_2[8]
        indice_2 = pruned_column_2[9]
        
        if limite_2 is not None and limite_2 != 'None':
            limite_2 = int(limite_2.strip("'"))
            limite_liquido.append(limite_2)

        if indice_2 is not None and indice_2 != 'None':
            indice_2 = int(indice_2.strip("'"))
            Indice_plasticidad.append(indice_2)
            

    encoded_image = ""
    
    encoded_image = cartaPlasticidad(limite_liquido, Indice_plasticidad)
    
    image_element = html.Img(src="data:image2/png;base64,{}".format(encoded_image))
    
    return html.Div([image_element])
            
              
#calculamos la curva granulométrica

# Actualizar la imagen en intervalos regulares
@app.callback(
    
    Output('curva_granulometrica', 'children'),
    Input('editing-columns', 'data')
)

def update_graph_image(columns):
    
    pruned_column_0 = []

    for row in columns:
        if row.get(0) != '':
            pruned_column_0.append(row.get('column-0'))

    pasa = []
    
    if len(pruned_column_0) >= 9:
        valor_0 = pruned_column_0[0]
        valor_1 = pruned_column_0[1]
        valor_2 = pruned_column_0[2]
        valor_3 = pruned_column_0[3]
        valor_4 = pruned_column_0[4]
        valor_5 = pruned_column_0[5]
        valor_6 = pruned_column_0[6]
        valor_7 = pruned_column_0[7]
    
    if valor_0 is not None and valor_0 != 'None':
        valor_0 = int(valor_0.strip("'"))
        pasa.append(valor_0)
    
    if valor_1 is not None and valor_1 != 'None':
        valor_0 = int(valor_1.strip("'"))
        pasa.append(valor_1)
    
    if valor_2 is not None and valor_2 != 'None':
        valor_0 = int(valor_2.strip("'"))
        pasa.append(valor_2)
    
    if valor_3 is not None and valor_3 != 'None':
        valor_0 = int(valor_3.strip("'"))
        pasa.append(valor_3)
    
    if valor_4 is not None and valor_4 != 'None':
        valor_0 = int(valor_4.strip("'"))
        pasa.append(valor_4)
    
    if valor_5 is not None and valor_5 != 'None':
        valor_0 = int(valor_5.strip("'"))
        pasa.append(valor_5)
    
    if valor_6 is not None and valor_6 != 'None':
        valor_0 = int(valor_6.strip("'"))
        pasa.append(valor_6)
    
    if valor_7 is not None and valor_7 != 'None':
        valor_0 = int(valor_7.strip("'"))
        pasa.append(valor_7)
    
    


    image_base64 = curvaGranulometrica(pasa)    
    image_element = html.Img(src="data:image/png;base64,{}".format(image_base64))    
    return html.Div([image_element])



if __name__ == '__main__':
    app.run_server(debug=True)
