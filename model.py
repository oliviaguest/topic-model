import csv, logging, gensim, bz2
import numpy as np
from pprint import pprint   # pretty-printer

with open('Manchester_for_Olivia_without_stopwords.txt', 'rb') as csvfile:
    # below I am asking for columns 1 and 7 *only* to be imported from the test file sent to me by Themis: Manchester_for_Olivia_without_stopwords.txt
    # currently there is a bug int he corpus and even though I think column 7 should be used I am using 6
    #data = np.genfromtxt(csvfile, delimiter=' ', dtype="|S16", usecols= [0, 7])
    data = np.genfromtxt(csvfile, delimiter=' ', dtype="|S16", usecols= [0, 6])

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

# remove words that appear only once, this is a common tactic as per tutorial on gensim website
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1] for text in texts]


dictionary = gensim.corpora.Dictionary(texts) # load id->word mapping (the dictionary)

dictionary.save('Manchester_for_Olivia_without_stopwords.dict') # store the dictionary, for future reference

corpus = [dictionary.doc2bow(text) for text in texts]# the corpus iterator
gensim.corpora.MmCorpus.serialize('Manchester_for_Olivia_without_stopwords.mm', corpus) # store to disk, for later use
#print(corpus)
#print(dictionary.token2id)

# the following few lines allows us to generate a vector representing an unseen document
new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec) # words that do not appeal in the dictionary are ignored

#dictionary.compactify() # remove gaps in id sequence after words that were removed --- not needed since I removed the singleton words before turning texts into dictionary
print(dictionary)
print(corpus)

# This is to load and run an LDA model
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# extract LDA topics
topics = 50
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=topics, update_every=1, chunksize=10, passes=10)
# print the most contributing words for 20 randomly selected topics
lda.print_topics(topics)
