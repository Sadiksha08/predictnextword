# -*- coding: utf-8 -*-
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
    
    unigrams = pickle.load(open("./pickle/unigramslist.pkl", 'rb'))
    #dfbiagramcolle1 = pickle.load(open("./pickle/dfbiagramcolle.pkl", 'rb'))
    #dfbiagramcolle = pd.DataFrame(dfbiagramcolle1) 
    #dftriagramcolle1= pickle.load(open("./pickle/dftriagramcolle.pkl", 'rb'))
    #dftriagramcolle = pd.DataFrame(dftriagramcolle1) 
    dfbiagramcolle = pd.read_pickle(r"./pickle/dfbiagramcolle.pkl")
    dftriagramcolle = pd.read_pickle(r"./pickle/dftriagramcolle.pkl")
    
    st.title("Prediction Results")
    number = st.sidebar.slider("Select the number of words to predict :", min_value=1, max_value = 10, value=5)
    word = st.sidebar.text_input(label = "Enter the Word/letters")
       
    if (st.sidebar.button("Predict")): 
        printinput = word
        #print("statement is: " + printinput)
        
        printinput=printinput.lower()
        printinput=printinput.translate(str.maketrans('','','01234567890'))
        #print(string.punctuation)
        #print(printinput)
        
        
        flaglist=string.punctuation   # storing the puctuation in list
        flag=0   # initialization 
        
        for i in range(len(flaglist)):    # if word end with from any punctuation from the flaglist
            if str.endswith(printinput,flaglist[i]):
                flag=flag+1   # it run unitl the flag list end
                
        #print("Flag is "+ str(flag))
        
        if flag==0 :   # if our input not ending with punctuation
            
            if str.endswith(printinput," ") :     # if input ends with space
                #print("Biagram and Triagram")
                # filter1 = dfbiagramcolle["Search1"]== printinput
                # filter2 = dftriagramcolle["Search1"]== printinput[1]
                frames = [dftriagramcolle, dfbiagramcolle]
                df = pd.concat(frames)    # storing bigram and trigram
                #print(dftriagramcolle.head())
                #print(dfbiagramcolle.head())
                printinput=printinput.strip()  # removing trailing and leading space
                printinput=printinput.translate(str.maketrans('','',string.punctuation)) # if there are any puctuation anywhere in between the text that also remove from here
                #print(len(printinput))
                words = printinput.split() # spliting the word if we type 5 word then store on position 
                #print(words)
                if len(words) == 1:   # after splitting if the word length is 1  then 
                    #print("Biagram and Triagram if")
                    df = df.loc[df['Search1']==words[0]] # it lock the the data frame and show the similar word to the
                else:
                    print("Biagram and Triagram else")  # emmma will check ----[emma]  [will] [check] ---  [will] [check] --- search
                    words= words[-2]+" "+words[-1]   # if after splitting the word length is more than word then it combine the last 2 word in search
                    print(words)
                    df = df.loc[df['Search1']==words] # then it lock and store the dataframe
                df.reset_index()
                df = df.sort_values(by='Freq',ascending=False)
                #print(df.head(10))
                selection = df[['Word', 'Freq', 'Next']] # store all data # creating new dataframe and storing the respective values and variable
                #print("Top 10 next word prediction is ")
                #print(selection.head(10))
                df_1=selection.head(number) # it will store that much data that we select on the slider
                df_1.reset_index()
                if len(df_1) >0:
                    st.text('Input Text:' + printinput) 
                    st.text('Prediction type: (3) [space] - Previous Word Complete; Predicts Next Word.')
                    st.text('Predicted Words:')
                    st.dataframe(df_1)
                    st.title("Bar Chart")
                    fig = plt.figure(figsize = (10, 5))
                    plt.barh(df_1['Word'], df_1['Freq'])
                    plt.xlabel("Number of Freq")
                    plt.ylabel("Words")    
                    plt.title("Word Freq Count") 
                    st.pyplot(fig)
                    st.title("Word Cloud")
                    # plot word cloud
                    # word cloud options
                    # https://www.datacamp.com/community/tutorials/wordcloud-python
                    #print('\n*** Plot Word Cloud - Top 100 ***')
                    d = {}
                    for a, x in df_1[['Word','Freq']].values:
                        d[a] = x 
                    print(d)
                    wordcloud = WordCloud(background_color="white")
                    wordcloud.generate_from_frequencies(frequencies=d)
                    fig = plt.figure(figsize = (10, 5))
                    plt.imshow(wordcloud, interpolation="bilinear")
                    plt.axis("off")
                    st.pyplot(fig)
                else:
                    st.text('Input Text:' + printinput)    # if we type that word which are not present in our input file then it will show this
                    st.text('No predicted Words found:')
            else :
                #print("Unigram")
                printinput=printinput.strip()  # # if the word is not ending with space then unigram call hoga then cleaning hoga
                printinput=printinput.translate(str.maketrans('','',string.punctuation))
                words = printinput.split() # splitting the word or sentence they said ending without space
                newlist =[]
                print(words)
                if len(words) == 1:  # if we type said without space so it will return same word # unigram
                    words=words[0]    # only type said the [0] postion [said[]]
                else:
                    words=words[-1]  # if typed they said then last word pick karega [-1] [said]
                print(words)
                for i in range(len(unigrams)):       # we are loading unigram from the pickle file (list wala upper code me) 
                    if str.startswith(unigrams[i],words) or (words==unigrams[i]): # said , sadest , .... etc will store
                        newlist.append(unigrams[i])
                dfnewlist = Counter(newlist)    # it will take unique words
                #print(newlist)
                
                if len(dfnewlist) >0:   # check df newlist size is greater then 0 
                    df  = pd.DataFrame.from_dict(dfnewlist, orient='index').reset_index()
                    df.columns = ['Word','Freq']
                    #print(df.head())
                    df = df.sort_values(by='Freq',ascending=False)
                    #print(df.head(10))
                    selection = df[['Word','Freq']]
                    #print("Top 10 next word prediction is ")
                    #print(selection.head(10))
                    df_1=selection.head(number)  # slider pe jo number daal rahe hai wo number aaega
                    df_1.reset_index()
                    st.text('Input Text:' + printinput) 
                    st.text('Prediction type: (2) [alphabet] - Word Maybe Incomplete; Predicts Current Word.')
                    st.text('Predicted Words:')
                    st.dataframe(df_1)
                    st.title("Bar Chart")
                    fig = plt.figure(figsize = (10, 5))
                    plt.barh(df_1['Word'], df_1['Freq'])
                    plt.xlabel("Number of Freq")
                    plt.ylabel("Words")    
                    plt.title("Word Freq Count")
                    st.pyplot(fig)
                    st.title("Word Cloud")
                    # plot word cloud
                    # word cloud options
                    # https://www.datacamp.com/community/tutorials/wordcloud-python
                    #print('\n*** Plot Word Cloud - Top 100 ***')
                    d = {}
                    for a, x in df_1[['Word','Freq']].values:
                        d[a] = x 
                    print(d)
                    wordcloud = WordCloud(background_color="white")
                    wordcloud.generate_from_frequencies(frequencies=d)
                    fig = plt.figure(figsize = (10, 5))
                    plt.imshow(wordcloud, interpolation="bilinear")
                    plt.axis("off")
                    st.pyplot(fig)
                else:
                    st.text('Input Text:' + printinput)   # if we enter word without space and wo word humare unigram file me hai hi nahi to it will give word not found
                    st.text('No predicted Words found:')  
    
        else:
            st.text('Input Text:' + word)    # if flag list greater than 0 that is if any puctuation you give while giving the input and not ending with space then it will print this no prediction due to punctuation
            st.text('No prediction due to punctuation')
            st.text('Prediction type: (1) [punctuation] - No Prediction.')
            #print("No prediction due to punctuation")
        
    st.sidebar.info("INSTRUCTIONS")
    st.sidebar.info('To predict next word, please type a sentence or a phrase.\n At least three chars requried. Use slider control to increase or decrease count of predicted words.\n For best results count should be 5 or more')
    
    
    st.sidebar.info('Word Prediction Is Based On The Last Character: (1) [punctuation] - No Prediction. (2) [alphabet] - Word Maybe Incomplete; Predicts Current Word. (3) [space] - Previous Word Complete; Predicts Next Word')

                 
