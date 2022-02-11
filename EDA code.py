# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:28:00 2021

@author: Sadiksha Singh
"""

#import nltk
#nltk.download('all')

# imports
import pandas as pd
from matplotlib import pyplot as plt
#%matplotlib inline
import seaborn as sns
from wordcloud import WordCloud

filename="output_file_gutenberg.txt"

fileList=['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']


#Merging file
with open(filename, 'w', encoding='ISO-8859-1') as outfile:
    for fname in fileList:
        with open('./gutenberg_dataset/'+fname , encoding='ISO-8859-1') as infile:
            for line in infile:
                outfile.write(line)


# file-input.py
print('\n*** Read File ***')
filename = 'output_file_gutenberg.txt'
file_name1 = './pickle/word_freq_output_file_gutenberg.pkl' 
f = open(filename ,'r', encoding='ISO-8859-1')
strAllTexts = f.read()
f.close()
print('Done ...')

# print file text
print('\n*** File Text ***')
# file text
print(strAllTexts)
# object type
print(type(strAllTexts))

#*********************************************************************************************

# Task 1 :file size
# using getsize function os.path module
import os

file_size = os.path.getsize(filename)
#print("File Size is :", file_size, "bytes")
print("File Size is :" + str(round(file_size / (1024 * 1024), 4)) + " MB ")

#*********************************************************************************************

# Task 2 - line count & non-empty line 

numLines = 0
numWords = 0
numChars = 0        

with open(filename, 'r', encoding="ISO-8859-1") as file:
    for line in file:
        wordsList = line.split()
        numLines += 1
        numWords += len(wordsList)
        numChars += len(line)

print("Lines: %i\nWords: %i\nCharacters: %i" % (numLines, numWords, numChars))


# non-empty line count

file = open(filename, 'r', encoding="ISO-8859-1")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
print(line_count)

# Another method

# file = open(filename, 'r', encoding="ISO-8859-1")
# nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# line_count = len(nonempty_lines)
# file.close()
# print(line_count)


#*********************************************************************************************

# Task 3 - character count 
# we will read a text file and count the number of characters in it.

#open file in read mode
file = open(filename, 'r', encoding="ISO-8859-1")

#read the content of file
data = file.read()

#get the length of the data
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)


#*********************************************************************************************

# Task 4 - nonwhite character count 
# we will read a text file and count the number of characters in it excluding 
# white space characters. 

#open file in read mode
file = open(filename, 'r', encoding="ISO-8859-1")

#read the content of file and replace spaces with nothing
data = file.read().replace(" ","")

#get the length of the data
number_of_nonwhite_characters = len(data)

print('Number of Nonwhite characters in text file :', number_of_nonwhite_characters)


#*********************************************************************************************

# Task 5 - word count per line - summary

# Python program to count 
# number of words in each line of a text  file separately
# Input filename, open it in 
# read mode. display its cntents 
# count and display number of  words

file = open(filename, "r", encoding="ISO-8859-1")

word_count = 0
i = 0
str1 = ""
#print("Contents of file " + str(file) + " are:")

# display and count number of  words in each line of text file
for line in file:
    i+=1
    #print(line, end='')
    words_in_line = len(line.split())
    str1 = str1 + "Words in Line Number " + str(i) + " are : " + str(words_in_line)+"\n"
    word_count+=words_in_line
    
print('\n\n ' + str1)    
print('\n\nTotal Number of  words in this file are = ' + str(word_count))
file.close()

# To Show the summary of word count per line
# Manually storing the output of str1 in excel file and splitting into two column Word in line number and Count

df = pd.read_csv(r'./word_count_per_line.csv')
print(df.head(10))
print(df.tail(10))

# info
print("\n*** Structure ***")
print(df.info())

# summary
print("\n*** Summary ***")
print(df.describe())
df.describe().apply(lambda s: s.apply('{0:.2f}'.format))


#*********************************************************************************************

# Task 6 -  word count

file = open(filename, "r", encoding="ISO-8859-1")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))

 
#*********************************************************************************************

# Task 7 - word count frequency

# split into words
from nltk.tokenize import word_tokenize
print('\n*** Split Text To Words ***')
lstAllWords = word_tokenize(strAllTexts)
# print file text
print(lstAllWords[0:100])
# print object type
print(type(lstAllWords))

# convert the tokens into lowercase: lower_tokens
print('\n*** Convert To Lower Case ***')
lstAllWords = [t.lower() for t in lstAllWords]
print(lstAllWords[0:100])

# retain alphabetic words: alpha_only
print('\n*** Remove Punctuations & Digits ***')
import string
lstAllWords = [t.translate(str.maketrans('','','01234567890')) for t in lstAllWords]
lstAllWords = [t.translate(str.maketrans('','',string.punctuation)) for t in lstAllWords]
print(lstAllWords[0:100])

# remove all stop words
# original found at http://en.wikipedia.org/wiki/Stop_words
print('\n*** Remove Stop Words ***')
import nltk.corpus
lstStopWords = nltk.corpus.stopwords.words('english')
lstAllWords = [t for t in lstAllWords if t not in lstStopWords]
print(lstAllWords[0:100])

# remove all bad words / pofanities ...
# original found at http://en.wiktionary.org/wiki/Category:English_swear_words
print('\n*** Remove Profane Words ***')
lstProfWords = ["arse","ass","asshole","bastard","bitch","bloody","bollocks","child-fucker","cunt","damn","fuck","goddamn","godsdamn","hell","motherfucker","shit","shitass","whore"]
lstAllWords = [t for t in lstAllWords if t not in lstProfWords]
print(lstAllWords[0:100])

# remove application specific words
print('\n*** Remove App Specific Words ***')
lstSpecWords = ['rt','via','http','https','mailto']
lstAllWords = [t for t in lstAllWords if t not in lstSpecWords]
print(lstAllWords[0:100])

# retain words with len > 3
print('\n*** Remove Short Words ***')
lstAllWords = [t for t in lstAllWords if len(t)>3]
print(lstAllWords[0:100])

# create a Counter with the lowercase tokens: bag of words - word freq count
print('\n*** Word Freq Count ***')
from collections import Counter
dctWordCount = Counter(lstAllWords)
#print(dctWordCount)

# print the 30 most common tokens
print('\n*** Word Freq Count - Top 30 ***')
print(dctWordCount.most_common(30))

# import WordNetLemmatizer
# https://en.wikipedia.org/wiki/Stemming
# https://en.wikipedia.org/wiki/Lemmatisation
# https://blog.bitext.com/what-is-the-difference-between-stemming-and-lemmatization/
print('\n*** Stemming & Lemmatization ***')
from nltk.stem import WordNetLemmatizer
# instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
# Lemmatize all tokens into a new list: lemmatized
lstAllWords = [wordnet_lemmatizer.lemmatize(t) for t in lstAllWords]
print(lstAllWords[0:100])

# create a Counter with the lowercase tokens: bag of words - word freq count
print('\n*** Word Freq Count ***')
dctWordCount = Counter(lstAllWords)
#print(dctWordCount)
print(type(dctWordCount))

# print the 30 most common tokens
print('\n*** Word Freq Count - Top 30 ***')
print(dctWordCount.most_common(30))
     
# conver dict to df
print('\n*** Convert To Dataframe ***')
dfWordCount  = pd.DataFrame.from_dict(dctWordCount, orient='index').reset_index()
dfWordCount.columns = ['Word','Freq']
print(dfWordCount.head(10))

# sort
print('\n*** Word Freq Count - Sorted ***')
dfWordCount = dfWordCount.sort_values('Freq',ascending=False)
print(dfWordCount.head(30))

import pandas as pd
import pickle
# Save dataframe to pickled pandas object
dfWordCount.to_pickle(file_name1) # where to save it usually as a .plk

# Load dataframe from pickled pandas object
df_1= pd.read_pickle(file_name1)
df_1.head(10)


# plot freq
# horizontal bar
print('\n*** Plot Word Freq Count - Top 30 ***')
plt.figure()
df = dfWordCount[0:30]
sns.barplot(x="Freq", y="Word", data=df, color="b", orient='h').set(title = "Word Freq Count - Top 30")
plt.show()


#****************************************************************************************************************************

# Task 9 - Word Cloud - Top 100 words 

# plot word cloud
# word cloud options
# https://www.datacamp.com/community/tutorials/wordcloud-python
print('\n*** Plot Word Cloud - Top 100 ***')
d = {}
for a, x in dfWordCount[0:100].values:
    d[a] = x 
print(d)
wordcloud = WordCloud(background_color="white")
wordcloud.generate_from_frequencies(frequencies=d)
plt.figure(figsize=[8,8])
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

#****************************************************************************************************************************

# Task 8 - frequency of word count frequency

# number of numbers in a given range
def getCount(list1, l, r):
    return len(list(x for x in list1 if l <= x < r))
 
# driver code
# freq distribution    
print('\n*** Word Freq Distribution ***')
from collections import OrderedDict
dfRange = pd.DataFrame(columns=['Range','Count'])
vStep = 5
vFrom = 1
vCount = -1
while (vCount != 0):
    vTill = vFrom + vStep
    vRange = str(vFrom) + " >= x > " + str(vTill)
    vCount = getCount(dfWordCount['Freq'], vFrom, vTill)    
    dfTmp = pd.DataFrame(OrderedDict({'Range':[vRange],'Count':[vCount]}))
    dfRange = pd.concat([dfRange,dfTmp])
    vFrom = vTill
# last one
vTill = dfWordCount['Freq'].max() + 1
vRange = str(vFrom) + " >= x > " + str(vTill)
vCount = getCount(dfWordCount['Freq'], vFrom, vTill)    
dfTmp = pd.DataFrame(OrderedDict({'Range':[vRange],'Count':[vCount]}))
dfRange = pd.concat([dfRange,dfTmp])
#  
dfRange.index = range(len(dfRange.index))
print(dfRange)
print(dfRange['Count'].sum())

# histogram
print('\n*** Word Freq Dist Histogram ***')
plt.figure()
#sns.distplot(dfWordCount['Freq'], size=5, kde=False, color='b')
sns.distplot(dfWordCount['Freq'], bins=len(dfRange)+1, kde=False, color='b')
#plt.ylim(0,50)
plt.show()
