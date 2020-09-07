import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div(children=[
    html.Div(children='''
        symbol to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),  # creates a place for input
    html.Div(id='output-graph')  # creates a place for output to go
])


@app.callback(  # indicates where the input is coming from and where output is going
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    try:
        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime.now()
        df = web.DataReader(input_data, 'yahoo', start, end)  # puts data in df
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        df = df.drop("High", axis='columns')
        return dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
                ],  # graphs time v closing price of stock
                'layout': {
                    'title': input_data
                }
            }
        )
    except:
        return


if __name__ == '__main__':
    app.run_server(debug=True)
