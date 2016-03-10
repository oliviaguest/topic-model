#import mdp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as sch
from heatmapcluster import heatmapcluster

from scipy import spatial
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine
import pickle
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
import csv, logging, gensim, bz2
from pprint import pprint   # pretty-printer

import openpyxl as xl


lda = pickle.load(open('output.pkl', 'r'))


CDI_words = ['book', 'brush', 'button', 'hair', 'key', 'window', 'foot', 'tongue', 'stone', 'bottle', 'box', 'bucket', 'banana', 'finger', 'arm', 'leg', 'brick', 'bin', 'broom', 'comb', 'hammer', 'scissors', 'ball', 'doll', 'radio', 'tea', 'train', 'sink', 'swing', 'telephone', 'bath', 'clock', 'jug', 'coat', 'dress', 'nose', 'pyjamas', 'shirt', 'sock', 'sweater', 'trousers', 'plate', 'eye', 'biscuit', 'cake', 'cheese', 'bed', 'chair', 'lamp', 'table', 'bowl', 'nail', 'rock', 'carrot', 'peas', 'ear', 'apple', 'coffee', 'pen', 'oven', 'toe', 'orange', 'milk', 'sofa', 'bread', 'jeans', 'cup', 'jam', 'necklace', 'mug', 'balloon', 'bicycle', 'boat', 'bus', 'butter', 'car', 'jacket', 'pillow', 'fridge', 'watch', 'spade', 'fork', 'motorcycle', 'truck', 'spoon', 'boots', 'duck', 'penguin', 'deer', 'elephant', 'giraffe', 'horse', 'turtle', 'dog', 'owl', 'cow', 'pony', 'monkey', 'mouse', 'rabbit', 'squirrel', 'bee', 'lion', 'goose', 'turkey', 'bear', 'cat', 'pig', 'donkey', 'sheep', 'spider', 'frog', 'butterfly', 'chicken', 'lamb', 'tiger']




wb1 = xl.load_workbook('CDI words.xlsx')
#print wb.get_sheet_names()
#print wb

sheet1 = wb1['Sheet1']
row_count1 = sheet1.get_highest_row() 
names = set()
for i in range(1,row_count1):
  #print sheet_ranges['A'+str(i)].value, sheet_ranges['B'+str(i)].value
  #features.add(sheet['B'+str(i)].value)
  names.add(sheet1['A'+str(i)].value)
  
print names  

CDI_words = names
rep = []


dictionary = gensim.corpora.Dictionary.load('Manchester_for_Olivia_without_stopwords.dict') # store the dictionary, for future reference

bow = dictionary.token2id


corpus_words = set(bow.keys())
intersection = corpus_words.intersection(CDI_words)
whats_left = corpus_words.union(CDI_words) - corpus_words.intersection(CDI_words)
whats_left = CDI_words - corpus_words.intersection(CDI_words)
whats_left = list(whats_left)
print whats_left
intersection = list(intersection)



for i, vec in enumerate(intersection):
  #CDI_words = ['cat']
  #print(CDI_words) # words that do not appeal in the dictionary are ignored


  doc_bow = dictionary.doc2bow([vec])#new_doc.lower().split())
  doc_lda = lda[doc_bow]
  doc_lda = lda.get_document_topics(doc_bow, minimum_probability=0)
  print i, doc_lda, '\n'
  doc_lda = [list(elem) for elem in doc_lda]
  rep.append( doc_lda)
  
rep = np.asarray(rep)
print rep.shape
representations = rep[:,:,1]
for i, vec in enumerate(intersection):
    print i, vec,  bow[vec], rep[i,:,1]






X = representations
label = intersection
# PCA time
pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)
PCA(copy=True, n_components=2, whiten=False)
print(pca.explained_variance_ratio_) 

fig = plt.figure(figsize=(20, 18))
ax = fig.add_subplot(111)
ax.scatter(X_r[:, 0], X_r[:, 1], c='w', label='Phonemes', marker='o', s = 75, alpha = 0.8 )
ax.set_ylim([-1.3, 1.3])
ax.set_xlim([-1.8, 1.8])
for i, txt in enumerate(label):
    #l = plt.Text(text=txt, fontproperties=fp, x = X_r[i, 0],y = X_r[i, 1], axes = ax, figure = fig)
    ax.annotate(txt, (X_r[i, 0], X_r[i, 1]), horizontalalignment='center', verticalalignment='center',size = 14, rotation = 90)
#for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
plt.legend()
plt.title('Phoneme PCA')
plt.xlabel('First Principal Component (explained variance ratio = '+str(np.around(pca.explained_variance_ratio_[0], decimals = 3))+')')
plt.ylabel('Second Principal Component (explained variance ratio = '+str(np.around(pca.explained_variance_ratio_[1], decimals = 3))+')')
fig.savefig('pca.png', bbox_inches='tight')
fig.savefig('pca.pdf', bbox_inches='tight')


#print phoneme
#print label
label = list(label)
#X = np.asarray(phoneme)
# generate the linkage matrix
Z = sch.linkage(X, 'ward')
c, coph_dists = sch.cophenet(Z, pdist(X, 'euclidean'))
# c, coph_dists = sch.cophenet(Z, pdist(X))
# Cophenetic Correlation Coefficient of clustering.
# This compares (correlates) the actual pairwise distances of all your samples to those implied by the hierarchical clustering.
# The closer the value is to 1, the better the clustering preserves the original distances.
print label, type(label[0])
print c

# calculate full dendrogram
fig = plt.figure(figsize=(15, 5))
ax = fig.add_subplot(111)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('International Phonetic Alphabet Phoneme')
plt.ylabel('Distance')
sch.dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=3.,  # font size for the x axis labels
    labels = label,
)

#ax.tick_params(labelsize=6)
#plt.show()

fig.savefig('dendrogram.png', bbox_inches='tight')
fig.savefig('dendrogram.pdf', bbox_inches='tight')

print len(label), rep.shape
#plt.show()
