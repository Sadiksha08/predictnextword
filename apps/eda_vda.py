# -- coding: utf-8 --
"""
Created on Tue Nov 16 01:10:12 2021

@author: Pushpa
"""
import streamlit as st 
import pickle
import string
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud

def app():

    
    dfWordCount= pd.read_pickle('./pickle/word_freq_output_file_gutenberg.pkl')
    dfunigramscolle= pd.read_pickle('./pickle/dfunigramscolle.pkl')
    dfbiagramcolle= pd.read_pickle('./pickle/dfbiagramcolle.pkl')
    dftriagramcolle= pd.read_pickle('./pickle/dftriagramcolle.pkl')
    df = dfWordCount[0:30]
    df1 = dfWordCount[0:100]
    # radio button
    vDispMode = st.sidebar.radio("",('Exploratory Data Analysis (EDA)','Visual Data Analysis (VDA)','Unigram','Bigram','Trigram'))

    # for Overview
    if (vDispMode == 'Exploratory Data Analysis (EDA)'):
        st.title("Exploratory Data Analysis (EDA)")
        st.text("1. File Size is :11.4458 MB")
        st.text("2. Line count :256893 ")
        st.text("3. Non-empty line count :206442")
        st.text("4. Character count :11744888")
        st.text("5. Nonwhite character count: 9744165")
        #st.text("6. Word count per line - summary: ")
        st.text("6. Number of words in text file : 2135242")
        #st.text("8. Word count frequency")
        
    if (vDispMode == 'Visual Data Analysis (VDA)'):
        st.title("Visual Data Analysis (VDA)")
        st.title("Word Freq Count - Top 30")
        fig = plt.figure(figsize = (10, 5))
        plt.barh(df['Word'], df['Freq'])
        plt.xlabel("Freq")
        plt.ylabel("Words")    
        st.pyplot(fig)
        st.title("Word Cloud - Top 100 words")
        d = {}
        for a, x in df1[['Word','Freq']].values:
            d[a] = x 
        wordcloud = WordCloud(background_color="white")
        wordcloud.generate_from_frequencies(frequencies=d)
        fig = plt.figure(figsize = (10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(fig)
        
    if (vDispMode == 'Unigram'):
        df = dfunigramscolle[0:30]
        df1 = dfunigramscolle[0:100]
        st.title("Unigram")
        st.title("Word Freq Count - Top 30")
        fig = plt.figure(figsize = (10, 5))
        plt.barh(df['Word'], df['Freq'])
        plt.xlabel("Freq")
        plt.ylabel("Words")    
        st.pyplot(fig)
        st.title("Word Cloud - Top 100 words")
        d = {}
        for a, x in df1[['Word','Freq']].values:
            d[a] = x 
        wordcloud = WordCloud(background_color="white")
        wordcloud.generate_from_frequencies(frequencies=d)
        fig = plt.figure(figsize = (10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(fig)
        
    if (vDispMode == 'Bigram'):
        df = dfbiagramcolle[0:30]
        df1 = dfbiagramcolle[0:100]
        st.title("Bigram")
        st.title("Word Freq Count - Top 30")
        fig = plt.figure(figsize = (10, 5))
        plt.barh(df['Word'], df['Freq'])
        plt.xlabel("Freq")
        plt.ylabel("Words")    
        st.pyplot(fig)
        st.title("Word Cloud - Top 100 words")
        d = {}
        for a, x in df1[['Word','Freq']].values:
            d[a] = x 
        wordcloud = WordCloud(background_color="white")
        wordcloud.generate_from_frequencies(frequencies=d)
        fig = plt.figure(figsize = (10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(fig)
    
    if (vDispMode == 'Trigram'):
        df = dftriagramcolle[0:30]
        df1 = dftriagramcolle[0:100]
        st.title("Trigram")
        st.title("Word Freq Count - Top 30")
        fig = plt.figure(figsize = (10, 5))
        plt.barh(df['Word'], df['Freq'])
        plt.xlabel("Freq")
        plt.ylabel("Words")    
        st.pyplot(fig)
        st.title("Word Cloud - Top 100 words")
        d = {}
        for a, x in df1[['Word','Freq']].values:
            d[a] = x 
        wordcloud = WordCloud(background_color="white")
        wordcloud.generate_from_frequencies(frequencies=d)
        fig = plt.figure(figsize = (10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(fig)
    
    
    
    
            
            
        
    
    
        
        