import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
stock = 'TSLA'
df = web.DataReader(stock,'yahoo', start, end)
app = dash.Dash()
app.layout = html.Div(children=[
    html.Div(children='''
        omg finance
    '''),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': df.index, 'y':df.Close, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
