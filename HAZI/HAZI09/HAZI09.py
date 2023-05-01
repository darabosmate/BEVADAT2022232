import numpy as np
from sklearn import datasets
from scipy.stats import mode
from numpy import ma
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

class KMeansOnDigits:
    def __init__(self,  n_clusters=10, random_state=0):
        self.n_clusters = n_clusters
        self.random_state = random_state


    def load_dataset(self):
        self.digits = datasets.load_digits()
    

    def predict(n_clusters:int,random_state:int,digits)-> (KMeans, np.ndarray):
        km = KMeans(n_clusters=n_clusters, random_state=random_state)
        self.clusters = km.fit_predict(self.digits.data)


    def get_labels(clusters:np.ndarray, digits)-> np.ndarray:
        result = np.zeros(clusters.shape[0])
        for i in range(10):
            ma_arr = ma.masked_equal(self.clusters, i)
            mod = mode(self.digits.target[mask], keepdims=False).mode
            result[ma_arr.mask] = mod

        return result


    def calc_accuracy(self):
        self.accuracy = np.round(accuracy_score(self.digits.target, self.clusters), decimals=2)


    def confusion_matrix(self):
        self.mat = conf_matrix(self.digits.target, self.clusters)