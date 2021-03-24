# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:31:57 2021

@author: AMIT
"""

import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name = "Word Cloud"

global datas
datas=pd.read_csv('D:/AMIT DOCS/Forsk Coding/cloud1.csv')
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")



def create_app_ui():
    global project_name
    main_layout = dbc.Container(
            
        dbc.Jumbotron(
                [
                    
                    html.H1(id = 'heading', children = project_name, className = 'display-3 mb-4',style={}),
                    html.Div([
            html.Img(src = app.get_asset_url('Frequent_word_cloud.png'))]),
            html.Marquee(id='text',children='This are the most used word ',style = {'width':'100%', 'height':50,'color':'green'}),
            html.H1(id='text1',children='This is Table of most used word ',style = {'width':'100%', 'height':50,'color':'blue'}),
            dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in datas.columns],
                        data=datas.to_dict('records'),
                        ),
            ],className = 'text-center'
                        
                
                ),
        className = 'mt-4'
        )

    return main_layout


    
def main():
    global app
    global project_name
    
    open_browser()
    app.layout = create_app_ui()
    app.title = project_name
    app.run_server()
    app = None
    project_name = None
if __name__ == '__main__':
    main()