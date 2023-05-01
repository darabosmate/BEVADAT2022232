import numpy as np
from sklearn import datasets
from scipy.stats import mode
from numpy import ma
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sns

class KMeansOnDigits:
    def __init__(self,  n_clusters=10, random_state=0):
        self.n_clusters = n_clusters
        self.random_state = random_state


    def load_dataset(self):
        self.digits = datasets.load_digits()
    

    def predict(self):
        km = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = km.fit_predict(self.digits.data)


    def get_labels(self):
        result = np.zeros(self.clusters.shape[0])
        for i in range(10):
            ma_arr = ma.masked_equal(self.clusters, i)
            mod = mode(self.digits.target[ma_arr.mask], keepdims=False).mode
            result[ma_arr.mask] = mod

        self.labels = result


    def calc_accuracy(self):
        self.accuracy = np.round(accuracy_score(self.digits.target, self.labels), decimals=2)


    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)