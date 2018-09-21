import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import random
import Trump_Tweets

app = dash.Dash()
tweet = Trump_Tweets.trump_tweet()

app.layout = html.Div(children=[
    html.H1(children='Magic Spoiler Count'),
    html.H1(id='tweet_feed'),
    dcc.Interval(
        id='run_time_interval',
        interval = 1 *1000,
        n_intervals = 1
        ),
    ])

@app.callback(Output('tweet_feed', 'children'),
            [Input('run_time_interval', 'n_intervals')
            ])
def update_metrics(n):
    return tweet


if __name__ == '__main__':
    app.run_server(debug=True)
