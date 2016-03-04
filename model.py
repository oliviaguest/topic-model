import csv, logging, gensim, bz2
import numpy as np
from pprint import pprint   # pretty-printer

#with open('Manchester_for_Olivia_without_stopwords.txt', 'rb') as csvfile:
with open('ManchesterCorpus_excluding_stopwords_ver2.txt', 'rb') as csvfile:
    # below I am asking for columns 1 and 7 *only* to be imported from the test file sent to me by Themis: Manchester_for_Olivia_without_stopwords.txt
    # currently there is a bug int he corpus and even though I think column 7 should be used I am using 6
    data = np.genfromtxt(csvfile, delimiter=' ', dtype="|S16", usecols= [0, 7])
    #data = np.genfromtxt(csvfile, delimiter=' ', dtype="|S16", usecols= [0, 6])

#discovering the unique names and making sure there are as many as it seems
unique_names = set(data[:,0])
unique_names = [ int(x) for x in unique_names ]
unique_names = list(unique_names)
unique_names.sort()
assert unique_names == range(1,len(unique_names)+1) # just checking the format is consistent with my guess, i.e., every unique name is associated with a number and the numbers are contiguous

#setting up how many documents in the corpus, this is one-to-one, so child==doc
texts = []
for name in unique_names:
  texts.append([])
  
#go through to change from long to wide, i.e., get a list per child/doc
for i, row in enumerate(data):
  texts[int(row[0])-1].append(row[1]) # this is obviously conditional on the codes used being 1-N as in the file Themis sent me, also as per assert statement 
print len(texts), len(texts[0]) 

#texts = [[word for word in text.lower().split() if word not in stoplist]
         #for text in texts]

# remove words that appear only once, this is a common tactic as per tutorial on gensim website
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token.lower() for token in text if frequency[token] > 1] for text in texts]

stoplist = ['go', 'get', 'oh', 'yes', 'yeah', 'want', 'put', 's', 'can', 'just', 'mummy', 'not', 'be', 'shall', 'know', 'look', 'like', 'well', 'will', 'see', 'dear', 'draw', 'make', 'come', 'huh', 'now', 'gonna', 'mama']
def det(x):
  if x in stoplist:
    return True
  else:
    return False
for doc in texts:
  #for word in doc:
    #word = word.lower()
    #print word
  doc[:] = [x for x in doc if not det(x)]

dictionary = gensim.corpora.Dictionary(texts) # load id->word mapping (the dictionary)

dictionary.save('Manchester_for_Olivia_without_stopwords.dict') # store the dictionary, for future reference

corpus = [dictionary.doc2bow(text) for text in texts]# the corpus iterator
gensim.corpora.MmCorpus.serialize('Manchester_for_Olivia_without_stopwords.mm', corpus) # store to disk, for later use
#print(corpus)
#print(dictionary.token2id)

# the following few lines allows us to generate a vector representing an unseen document
new_doc = "trousers"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec) # words that do not appeal in the dictionary are ignored

#dictionary.compactify() # remove gaps in id sequence after words that were removed --- not needed since I removed the singleton words before turning texts into dictionary
print(dictionary)
print(corpus)

# This is to load and run an LDA model
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# extract LDA topics
topics = 5
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=topics, update_every=1, chunksize=10, passes=10)
# print the most contributing words for 20 randomly selected topics
lda.print_topics(topics)
## the following few lines allows us to generate a vector representing an unseen document
#new_doc = "trousers"

new_vec = ['book', 'brush', 'button', 'hair', 'key', 'window', 'foot', 'tongue', 'stone', 'bottle', 'box', 'bucket', 'banana', 'finger', 'arm', 'leg', 'brick', 'bin', 'broom', 'comb', 'hammer', 'scissors', 'ball', 'doll', 'radio', 'tea', 'train', 'sink', 'swing', 'telephone', 'bath', 'clock', 'jug', 'coat', 'dress', 'nose', 'pyjamas', 'shirt', 'sock', 'sweater', 'trousers', 'plate', 'eye', 'biscuit', 'cake', 'cheese', 'bed', 'chair', 'lamp', 'table', 'bowl', 'nail', 'rock', 'carrot', 'peas', 'ear', 'apple', 'coffee', 'pen', 'oven', 'toe', 'orange', 'milk', 'sofa', 'bread', 'jeans', 'cup', 'jam', 'necklace', 'mug', 'balloon', 'bicycle', 'boat', 'bus', 'butter', 'car', 'jacket', 'pillow', 'fridge', 'watch', 'spade', 'fork', 'motorcycle', 'truck', 'spoon', 'boots', 'duck', 'penguin', 'deer', 'elephant', 'giraffe', 'horse', 'turtle', 'dog', 'owl', 'cow', 'pony', 'monkey', 'mouse', 'rabbit', 'squirrel', 'bee', 'lion', 'goose', 'turkey', 'bear', 'cat', 'pig', 'donkey', 'sheep', 'spider', 'frog', 'butterfly', 'chicken', 'lamb', 'tiger']

for i, vec in enumerate(new_vec):
  #new_vec = ['cat']
  #print(new_vec) # words that do not appeal in the dictionary are ignored


  doc_bow = dictionary.doc2bow([vec])#new_doc.lower().split())
  doc_lda = lda[doc_bow]
  print i, doc_lda, '\n'
  
#2016-03-01 19:24:49,087 : INFO : topic #0 (0.100): 0.164*car + 0.081*go + 0.034*one + 0.033*trailer + 0.033*brumm + 0.031*Mummy + 0.030*bridge + 0.028*vehicle + 0.019*drive + 0.018*beep
#2016-03-01 19:24:49,087 : INFO : topic #1 (0.100): 0.068*go + 0.050*get + 0.046*can + 0.037*yeah + 0.029*not + 0.025*Nicole + 0.022*want + 0.020*now + 0.019*well + 0.019*come
#2016-03-01 19:24:49,088 : INFO : topic #2 (0.100): 0.068*yeah + 0.063*oh + 0.044*go + 0.037*Mummy + 0.035*baby + 0.022*want + 0.022*get + 0.018*s + 0.018*right + 0.018*look
#2016-03-01 19:24:49,088 : INFO : topic #3 (0.100): 0.046*oh + 0.042*go + 0.028*cow + 0.026*tiger + 0.024*look + 0.023*horse + 0.022*animal + 0.021*one + 0.018*can + 0.016*monkey
#2016-03-01 19:24:49,088 : INFO : topic #4 (0.100): 0.042*oh + 0.036*Mummy + 0.035*read + 0.028*s + 0.028*ambulance + 0.026*say + 0.024*look + 0.022*one + 0.020*book + 0.017*right
#2016-03-01 19:24:49,089 : INFO : topic #5 (0.100): 0.066*yes + 0.037*Ruth + 0.027*like + 0.027*put + 0.027*egg + 0.023*eat + 0.019*shop + 0.018*darling + 0.017*doll + 0.017*thank_you
#2016-03-01 19:24:49,089 : INFO : topic #6 (0.100): 0.064*one + 0.036*put + 0.032*oh + 0.031*get + 0.030*yes + 0.029*right + 0.023*make + 0.022*can + 0.022*now + 0.021*want
#2016-03-01 19:24:49,089 : INFO : topic #7 (0.100): 0.062*Warren + 0.058*go + 0.032*train + 0.028*oh + 0.026*s + 0.019*Mummy + 0.018*get + 0.016*man + 0.016*be + 0.016*Henry
#2016-03-01 19:24:49,090 : INFO : topic #8 (0.100): 0.030*yes + 0.026*yeah + 0.019*see + 0.019*s + 0.017*look + 0.016*Mummy + 0.015*one + 0.014*Daddy + 0.014*can + 0.013*go
#2016-03-01 19:24:49,090 : INFO : topic #9 (0.100): 0.084*oh + 0.033*get + 0.030*yes + 0.030*one + 0.024*can + 0.021*want + 0.018*go + 0.017*Caroline + 0.016*yeah + 0.015*just
