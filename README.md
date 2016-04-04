# LSI and LDA modelling
This repository contains some basic topic modelling (using the [gensim library](http://radimrehurek.com/gensim/)) in Python.
The corpus is based on the Manchester child language corpus (downloaded from the CHILDES website: http://childes.psy.cmu.edu/).

# How to run

## Topic modeling
To create the LDA model and save the to file, run:
```
python model.py lda
```
Or if you prefer to run LSI/LSA, run:
```
python model.py lsi
```

## Clustering
To generate the figures and save them to file, run: 

```
python clustering.py
```

# Figures
##Dendrogram

![Dendrogram](https://raw.githubusercontent.com/oliviaguest/topic-model/master/dendrogram.png)

##PCA

![Dendrogram](https://raw.githubusercontent.com/oliviaguest/topic-model/master/pca.png)
