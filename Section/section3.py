# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:08:02 2021

@author: AMIT
"""

# Importing the libraries
import pickle
import pandas as pd
import webbrowser
# !pip install dash
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output , State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


# Declaring Global variables
project_name = None
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Defining My Functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('D:/AMIT DOCS/Forsk Coding/csv/Scrapped_reviews.csv')
    global data
    data=scrappedReviews['Review_text'].sample(1000).tolist()
    global pickle_model
    file = open("pickle_model.pkl", 'rb') 
    pickle_model = pickle.load(file)

    global vocab
    file = open("feature.pkl", 'rb') 
    vocab = pickle.load(file)

def check_review(reviewText):

    #reviewText has to be vectorised, that vectorizer is not saved yet
    #load the vectorize and call transform and then pass that to model preidctor
    #load it later

    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))


    # Add code to test the sentiment of using both the model
    # 0 == negative   1 == positive
    
    return pickle_model.predict(vectorised_review)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_app_ui():
    main_layout = html.Div(
    [
    
    
    html.H3(children = 'Sentiment Analysis with Insights(DropDown)', id='result',style = {'textAlign': 'center','background-color':'yellow'}),
    html.Marquee(id='text',children='Lets predict the Sentiment ',style = {'width':'100%', 'height':50,'color':'grey'}),
    html.Br(),
    dcc.Dropdown(id='DropDown',options=[{'label': k, 'value': k} for k in (data)],style = {"margin-left": "100px",'width':1000, 'height':50}),
    html.Br(),
    html.Marquee(id='text1',children='The Prediction is made down ',style = {'width':'100%','height':50,'color':'blue'}),

    html.H3(children = 'Positive/Negative for drop down', id='result2',style = {'textAlign': 'center','width':'100%', 'height':50}),

   
    ]    
    )
    
    return main_layout



    
@app.callback(
    
    Output( 'result2'   , 'children'     ),
    Output('result2','style'),
    [
    Input( 'DropDown'    ,  'value'    )
    
    ]
    )   
def update_app_ui_3(value):

    print("Data Type = ", str(type(value)))
    print("Value = ", str(value))
    response = check_review(value)
    if (response[0] == 0):
        result = 'Negative'
        style= {"margin-left": "600px",'width':500, 'height':50,'color':'red'}
    elif (response[0] == 1 ):
        result = 'Positive'
        style= {"margin-left": "600px",'width':500, 'height':50,'color':'green'}

    else:
        result = 'Unknown'
        style=style = {"margin-left": "500px",'width':1500, 'height':50,'background-color':'grey'}

    return result,style
        

    
    
    


# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    open_browser()
    #update_app_ui()
    
    
    global scrappedReviews
    global project_name
    global app
    global random_1000
    
    project_name = "Sentiment Analysis with Insights"
    #print("My project name = ", project_name)
    #print('my scrapped data = ', scrappedReviews.sample(5) )
    
    # favicon  == 16x16 icon ----> favicon.ico  ----> assests
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server()
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    random_1000=None
        
# Calling the main function 
if __name__ == '__main__':
    main()
    
    
    