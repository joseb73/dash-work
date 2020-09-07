# creating a webpage, with Dash framework, to auto update text output field based on input
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input', value='Enter something here!', type='text'),  # place for input
    html.Div(id='output')  # place to store output
])


@app.callback(  # how we autoupdate the webpage from input with a wrapper class
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):  # function being wrapped that simply outputs the given input
    return 'Input: "{}"'.format(input_data)


if __name__ == '__main__':
    app.run_server(debug=True)
