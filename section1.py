# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:24:46 2021

@author: AMIT
"""
import numpy as np
import pickle
import pandas as pd
import webbrowser
# !pip install dash
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output , State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

global data
data=pd.read_csv("D:/AMIT DOCS/Forsk Coding/csv/Scrapped_reviews.csv")


global pickle_model
file = open("pickle_model.pkl", 'rb') 
pickle_model = pickle.load(file)

global vocab
file = open("feature.pkl", 'rb') 
vocab = pickle.load(file)
reviewText=data.iloc[:, 0]
    
transformer = TfidfTransformer()
loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
vectorised_review = transformer.fit_transform(loaded_vec.fit_transform(reviewText))   
pred=pickle_model.predict(vectorised_review)  
data['Positivity']  =pred
data['Sentiment']  =None


data['Sentiment']=np.where(data['Positivity']==1,'Positive','Negative')
global pie_data
pie_data=data['Sentiment']
####
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_app_ui():
    main_layout = html.Div([
        html.H1(id='Main_title', children = "PIE CHART OF SCRAPPED REVIEWS",style = {'textAlign': 'center','background-color':'pink'}),
            
        dcc.Graph(id='Pie',figure=px.pie(data_frame=data,names=data['Sentiment'])),
        html.H1(id='name',children='This is the Pie chart ',style={"margin-left": "455px",'width':'520px'}),
        html.H1(id='name1',children='for Etsy review ',style={"margin-left": "500px",'width':'520px'})
        
     ]
        
    )
    
    return main_layout





def main():
    print("Start of your project")
    
    open_browser()
    #update_app_ui()
    
    
    global scrappedReviews
    global app
    
    project_name = "Sentiment Analysis with Insights"
    #print("My project name = ", project_name)
    #print('my scrapped data = ', scrappedReviews.sample(5) )
    
    # favicon  == 16x16 icon ----> favicon.ico  ----> assests
    app.layout = create_app_ui()
    app.run_server()
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    
        
# Calling the main function 
if __name__ == '__main__':
    main()










