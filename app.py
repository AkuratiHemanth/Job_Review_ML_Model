import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


data = pd.read_csv('/workspaces/Job_Review_ML_Model/glassdoor_reviews.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Bubble Chart"),
    dcc.Graph(id='bubble-chart'),
    html.Div(id='bubble-click-output'),
])

@app.callback(
    Output('bubble-chart', 'figure'),
    [Input('bubble-chart', 'clickData')]
)
def update_bubble_chart(click_data):
    fig = px.scatter(
        data,
        x="culture_values",
        y="work_life_balance",
        size="career_opp",
        text="firm",
        title="Interactive Bubble Chart",
        hover_name="firm",
        labels={'culture_values': 'Culture Values', 'work_life_balance': 'Work-Life Balance'},
    )
    return fig

@app.callback(
    Output('bubble-click-output', 'children'),
    [Input('bubble-chart', 'clickData')]
)
def display_click_data(click_data):
    if click_data is None:
        return "Click on a bubble to see corresponding information."
    point_data = click_data['points'][0]
    selected_firm = point_data['hovertext']
    selected_review = f"Culture Values: {point_data['x']}, Work-Life Balance: {point_data['y']}"
    return f"Selected Firm: {selected_firm}<br>Review Information: {selected_review}"

if __name__ == '__main__':
    app.run_server(debug=True)

