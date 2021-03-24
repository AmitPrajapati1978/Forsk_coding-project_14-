# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:50:42 2021

@author: AMIT
"""

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
global list
list=['Negative','Red','Positive','Green']
# Defining My Functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrappedReviews.csv')
    global data
    data=scrappedReviews['reviews'].tolist()
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
    html.H1(id='Main_title', children = "Sentiment Analysis with Insights",style = {'textAlign': 'center','background-color':'pink'}),
    html.Marquee(id='text',children='Lets predict the Sentiment ',style = {'width':'100%', 'height':50,'color':'grey'}),

    dcc.Textarea(
        id = 'textarea_review',
        placeholder = 'Enter the review here.....',
        style = {"margin-left": "125px",'width':1000, 'height':100}
        ),
    
    dbc.Button(
        children = 'Submit',
        id = 'button_review',
        color = 'dark',
        style={"margin-left": "525px",'width':'220px'}
        ),
    html.Tr(),
    html.Marquee(id='text1',children='The Prediction is made down ',style = {'width':'100%','height':50,'color':'blue'}),
   
    html.H3(children = 'Positive/Negative', id='result',style = {'textAlign': 'center','width':'100%', 'height':50}),
    
    
    ]    
    )
    
    return main_layout




@app.callback(
    Output( 'result'   , 'children'     ),
    Output('result','style'),
   
    [
    Input( 'button_review'    ,  'n_clicks'    )
    ],
    [
    State( 'textarea_review'  ,   'value'  )
    ]
    )
def update_app_ui_2(n_clicks, textarea_value):

    print("Data Type = ", str(type(n_clicks)))
    print("Value = ", str(n_clicks))


    print("Data Type = ", str(type(textarea_value)))
    print("Value = ", str(textarea_value))


    if (n_clicks > 0):
        global response

        response = check_review(textarea_value)
        if (response[0] == 0):
            result = 'The above review is Negative'
            style= {"margin-left": "450px",'width':500, 'height':50,'color':'red'}

        elif (response[0] == 1 ):
            result = 'The above review is Positive'
            style={"margin-left": "450px",'width':500, 'height':50,'color':'green'}

        else:
            result = 'Unknown'
            style== {"margin-left": "500px",'width':150, 'height':50,'background-color':'grey'}
        
        return result,style
        
    else:
        return ""
    

    
    


# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    open_browser()
    #update_app_ui()
    
    
    global scrappedReviews
    global project_name
    global app
    
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
    
        
# Calling the main function 
if __name__ == '__main__':
    main()
    