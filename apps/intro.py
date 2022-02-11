# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 00:10:44 2021

@author: Priya
"""
# import streamlit
import streamlit as st
from PIL import Image

    

def app():
    # subheader
    #st.subheader("NEXT WORD PREDICTOR")
    
    st.write("Wouldn’t it be cool for your system to predict what could be the next word that you are planning to type?")
    st.write("Next Word Prediction or what is also called Language Modeling is the task of predicting what word comes next. It is one of the fundamental tasks of NLP and has many applications. You might be using it daily when you write texts or emails without realizing it.")
    st.write("Predicting the most probable word for immediate selection is one of the most valuable technique for enhancing the communication experience. With growth in mobile technologies and vast spread of the internet, socializing has become much easier. People around the world spend more and more time on their mobile devices for email, social networking, banking and a variety of other activities. Due to fast paced nature of such conversation it is necessary to save as much as time possible while typing. Hence a predictive text application is necessary for this. Text prediction is one of the most commonly used techniques for increasing the rate of communication.")
    st.write("The ability of predicting the next word based upon its adjacent words is one of the fundamental task in natural language processing (NLP). In NLP the major focus is on understanding and determining how the interaction between human and a computer can be optimized. As humans, we tend to use language based upon the situation we are presented with. Selection of our next word depends upon a set of previous words. The goal of this research is to replicate a similar behavior of human word selection into a natural language processing model. Suggestions of new words that might be used are generated based upon the previous set of words. We started the project by analyzing the data followed by the pre-processing of the data. We will then tokenize this data and finally build the deep learning model. To achieve this goal, the N-Grams model is used. We assign frequency to each word and select the next word with highest frequency values. This frequency values are generated based upon the sequence of previous words. These sequences are known as N-Grams where N is the value which may be a unigram, bigram, trigram.")
    
    image = Image.open('./nwp.jpeg')
    st.image(image, caption='Next Word Predictor')
        
    



    