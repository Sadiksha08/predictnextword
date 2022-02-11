# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:28:00 2021

@author: Pushpa Yadav
"""

# imports
import pandas as pd
from matplotlib import pyplot as plt
#%matplotlib inline
import seaborn as sns
from wordcloud import WordCloud
import re

def generate_ngrams(words_list, n):
    ngrams_list = []
 
    for num in range(0, len(words_list)):
        ngram = ' '.join(words_list[num:num + n])
        ngrams_list.append(ngram)
 
    return ngrams_list

# filename="output_file_gutenberg.txt"

# fileList=['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']


# #Merging file
# with open(filename, 'w', encoding='ISO-8859-1') as outfile:
#     for fname in fileList:
#         with open('./Data/'+fname , encoding='ISO-8859-1') as infile:
#             for line in infile:
#                 outfile.write(line)



# file-input.py
print('\n*** Read File ***')
f = open('./output_file_gutenberg.txt','r' , encoding='ISO-8859-1')
strAllTexts = f.read()
f.close()
print('Done ...')

# split into words
from nltk.tokenize import word_tokenize
print('\n*** Split Text To Words ***')
lstAllWords = word_tokenize(strAllTexts)    

# convert the tokens into lowercase: lower_tokens
print('\n*** Convert To Lower Case ***')
lstAllWords = [t.lower() for t in lstAllWords]
lstAllWords = [t.strip() for t in lstAllWords]
lstAllWords = [t for t in lstAllWords if t != ' ']
print(lstAllWords[0:100])

# retain alphabetic words: alpha_only
print('\n*** Remove Punctuations & Digits ***')
import string
lstAllWords = [t.translate(str.maketrans('','','01234567890')) for t in lstAllWords]
lstAllWords = [t.translate(str.maketrans('','',string.punctuation)) for t in lstAllWords]
lstAllWords = [t.translate(str.maketrans('',''," ")) for t in lstAllWords]
lstAllWords = [t for t in lstAllWords if t != '']


# # remove application specific words
# print('\n*** Remove App Specific Words ***')
# lstSpecWords = ['rt','via','http','https','mailto']
# lstAllWords = [t for t in lstAllWords if t not in lstSpecWords]

# retain words with len > 0
print('\n*** Remove Short Words ***')
lstAllWords = [t for t in lstAllWords if len(t)>0]

unigrams = generate_ngrams(lstAllWords, 1)
import pickle
print(unigrams[0:50])
print(len(unigrams))


with open('./pickle/unigramslist.pkl', 'wb') as filepkl:
      
    # A new file will be created
    pickle.dump(unigrams, filepkl)

unigramslist = pickle.load(open("./pickle/unigramslist.pkl", 'rb'))
print(unigramslist[0:50])
# create a Counter with the lowercase tokens: bag of words - word freq count
print('\n*** Word Freq Count ***')
from collections import Counter
unigramscolle = Counter(unigrams)
print(len(unigramscolle))



# print the 10 most common tokens
print('\n*** Word Freq Count - Top 10 ***')
print(unigramscolle.most_common(10))
     
# conver dict to df
print('\n*** Convert To Dataframe ***')
dfunigramscolle  = pd.DataFrame.from_dict(unigramscolle, orient='index').reset_index()
dfunigramscolle.columns = ['Word','Freq']
print(dfunigramscolle.head(50))


# sort
print('\n*** Word Freq Count - Sorted ***')
dfunigramscolle = dfunigramscolle.sort_values(by='Freq',ascending=False)
print(dfunigramscolle.head(50))

dfunigramscolle.to_pickle('./pickle/dfunigramscolle.pkl')

# plot freq
# horizontal bar
print('\n*** Plot Word Freq Count - Top 30 ***')
plt.figure()
df = dfunigramscolle[0:30]
sns.barplot(x="Freq", y="Word", data=df, color="b", orient='h')
plt.show()

# plot word cloud
# word cloud options
# https://www.datacamp.com/community/tutorials/wordcloud-python
print('\n*** Plot Word Cloud - Top 100 ***')
d = {}
for a, x in dfunigramscolle[0:100].values:
    d[a] = x 
print(d)
wordcloud = WordCloud(background_color="white")
wordcloud.generate_from_frequencies(frequencies=d)
plt.figure(figsize=[8,8])
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

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
    vCount = getCount(dfunigramscolle['Freq'], vFrom, vTill)    
    dfTmp = pd.DataFrame(OrderedDict({'Range':[vRange],'Count':[vCount]}))
    dfRange = pd.concat([dfRange,dfTmp])
    vFrom = vTill
# last one
vTill = dfunigramscolle['Freq'].max() + 1
vRange = str(vFrom) + " >= x > " + str(vTill)
vCount = getCount(dfunigramscolle['Freq'], vFrom, vTill)    
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
sns.distplot(dfunigramscolle['Freq'], bins=len(dfRange)+1, kde=False, color='b')
#plt.ylim(0,50)
plt.show()

####################################################################################

#Biagram

biagram = generate_ngrams(lstAllWords, 2)
print(biagram[0:50])
print(len(biagram))


# create a Counter with the lowercase tokens: bag of words - word freq count
print('\n*** Word Freq Count ***')
from collections import Counter
biagramcolle = Counter(biagram)
print(len(biagramcolle))


# print the 10 most common tokens
print('\n*** Word Freq Count - Top 10 ***')
print(biagramcolle.most_common(10))
     
# conver dict to df
print('\n*** Convert To Dataframe ***')
dfbiagramcolle  = pd.DataFrame.from_dict(biagramcolle, orient='index').reset_index()
dfbiagramcolle.columns = ['Word','Freq']
print(dfbiagramcolle.head(50))

dfbiagramcolle['Search1']=dfbiagramcolle.Word.str.split(' ').str[0]
dfbiagramcolle['Next']=dfbiagramcolle.Word.str.split(' ').str[1]

# sort
print('\n*** Word Freq Count - Sorted ***')
dfbiagramcolle = dfbiagramcolle.sort_values(by='Freq',ascending=False)
print(dfbiagramcolle.head(10))

dfbiagramcolle.to_pickle('./pickle/dfbiagramcolle.pkl')


# plot freq
# horizontal bar
print('\n*** Plot Word Freq Count - Top 30 ***')
plt.figure()
df = dfbiagramcolle[0:30]
sns.barplot(x="Freq", y="Word", data=df, color="b", orient='h')
plt.show()

dfbiagramcollewc=dfbiagramcolle[['Word','Freq']]
print(dfbiagramcollewc.head())

# plot word cloud
# word cloud options
# https://www.datacamp.com/community/tutorials/wordcloud-python
print('\n*** Plot Word Cloud - Top 100 ***')
d = {}
for a, x in dfbiagramcollewc[0:100].values:
    d[a] = x 
wordcloud = WordCloud(background_color="white")
wordcloud.generate_from_frequencies(frequencies=d)
plt.figure(figsize=[8,8])
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


 
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
    vCount = getCount(dfbiagramcolle['Freq'], vFrom, vTill)    
    dfTmp = pd.DataFrame(OrderedDict({'Range':[vRange],'Count':[vCount]}))
    dfRange = pd.concat([dfRange,dfTmp])
    vFrom = vTill
# last one
vTill = dfbiagramcolle['Freq'].max() + 1
vRange = str(vFrom) + " >= x > " + str(vTill)
vCount = getCount(dfbiagramcolle['Freq'], vFrom, vTill)    
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
sns.distplot(dfbiagramcolle['Freq'], bins=len(dfRange)+1, kde=False, color='b')
#plt.ylim(0,50)
plt.show()


#############################################################################

#Triagram


triagram = generate_ngrams(lstAllWords, 3)
print(triagram[0:50])
print(len(triagram))


# create a Counter with the lowercase tokens: bag of words - word freq count
print('\n*** Word Freq Count ***')
triagramcolle = Counter(triagram)
print(len(triagramcolle))


# print the 10 most common tokens
print('\n*** Word Freq Count - Top 10 ***')
print(triagramcolle.most_common(10))
     
# conver dict to df
print('\n*** Convert To Dataframe ***')
dftriagramcolle  = pd.DataFrame.from_dict(triagramcolle, orient='index').reset_index()
dftriagramcolle.columns = ['Word','Freq']
print(dftriagramcolle.head(50))

dftriagramcolle['Search1']=dftriagramcolle.Word.str.split(' ').str[0] + " " + dftriagramcolle.Word.str.split(' ').str[1]
dftriagramcolle['Next']=dftriagramcolle.Word.str.split(' ').str[2]

# sort
print('\n*** Word Freq Count - Sorted ***')
dftriagramcolle = dftriagramcolle.sort_values(by='Freq',ascending=False)
print(dftriagramcolle.head(50))

dftriagramcolle.to_pickle("./pickle/dftriagramcolle.pkl")

# plot freq
# horizontal bar
print('\n*** Plot Word Freq Count - Top 30 ***')
plt.figure()
df = dftriagramcolle[0:30]
sns.barplot(x="Freq", y="Word", data=df, color="b", orient='h')
plt.show()

dftriagramcollewc=dftriagramcolle[['Word','Freq']]

# plot word cloud
# word cloud options
# https://www.datacamp.com/community/tutorials/wordcloud-python
print('\n*** Plot Word Cloud - Top 100 ***')
d = {}
for a, x in dftriagramcollewc[0:100].values:
    d[a] = x 
print(d)
wordcloud = WordCloud(background_color="white")
wordcloud.generate_from_frequencies(frequencies=d)
plt.figure(figsize=[8,8])
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

 
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
    vCount = getCount(dftriagramcolle['Freq'], vFrom, vTill)    
    dfTmp = pd.DataFrame(OrderedDict({'Range':[vRange],'Count':[vCount]}))
    dfRange = pd.concat([dfRange,dfTmp])
    vFrom = vTill
# last one
vTill = dftriagramcolle['Freq'].max() + 1
vRange = str(vFrom) + " >= x > " + str(vTill)
vCount = getCount(dftriagramcolle['Freq'], vFrom, vTill)    
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
sns.distplot(dftriagramcolle['Freq'], bins=len(dfRange)+1, kde=False, color='b')
#plt.ylim(0,50)
plt.show()

printinput = input("Enter statement:")
print("statement is: " + printinput)

printinput=printinput.lower()
printinput=printinput.translate(str.maketrans('','','01234567890'))


print(string.punctuation)
print(printinput)

flaglist=string.punctuation
flag=0

for i in range(len(flaglist)):
    if str.endswith(printinput,flaglist[i]):
        flag=flag+1
        
print("Flag is "+ str(flag))

if flag==0 :
    if str.endswith(printinput," ") :
        print("Biagram and Triagram")
        # filter1 = dfbiagramcolle["Search1"]== printinput
        # filter2 = dftriagramcolle["Search1"]== printinput[1]
        frames = [dftriagramcolle, dfbiagramcolle]
        df = pd.concat(frames)
        #print(dftriagramcolle.head())
        #print(dfbiagramcolle.head())
        printinput=printinput.strip()
        printinput=printinput.translate(str.maketrans('','',string.punctuation))
        print(len(printinput))
        words = printinput.split()
        print(words)
        if len(words) == 1:
            print("Biagram and Triagram if")
            df = df.loc[df['Search1']==words[0]]
        else:
            print("Biagram and Triagram else")
            words= words[-2]+" "+words[-1]
            print(words)
            df = df.loc[df['Search1']==words]
        df.reset_index()
        df = df.sort_values(by='Freq',ascending=False)
        #print(df.head(10))
        selection = df[['Word', 'Freq', 'Next']]
        print("Top 10 next word prediction is ")
        print(selection.head(10))
    else :
        print("Unigram")
        printinput=printinput.strip()
        printinput=printinput.translate(str.maketrans('','',string.punctuation))
        words = printinput.split()
        newlist =[]
        print(words)
        if len(words) == 1:
            words=words[0]
        else:
            words=words[-1]
        print(words)
        for i in range(len(unigrams)):       
            if str.startswith(unigrams[i],words) or (words==unigrams[i]):
                newlist.append(unigrams[i])
        dfnewlist = Counter(newlist)
        #print(newlist)
        df  = pd.DataFrame.from_dict(dfnewlist, orient='index').reset_index()
        df.columns = ['Word','Freq']
        #print(df.head())
        df = df.sort_values(by='Freq',ascending=False)
        #print(df.head(10))
        selection = df[['Word','Freq']]
        print("Top 10 next word prediction is ")
        print(selection.head(10))
else:
    print("No prediction due to punctuation")

  