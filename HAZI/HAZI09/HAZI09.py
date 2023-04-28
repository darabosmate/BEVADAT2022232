import numpy as np
from sklearn import datasets

class KMeansOnDigits:
    def __init__(self,  n_clusters=10, random_state=0):
        self.n_clusters = n_clusters
        self.random_state = random_state


    def load_dataset(self):
        self.digits = datasets.load_digits()
    
    def predict(n_clusters:int,random_state:int,digits)-> (KMeans, np.ndarray):
        km = KMeans(n_clusters=n_clusters, random_state=random_state)
        self.clusters = km.fit_predict(digits)
        
    def get_labels(clusters:np.ndarray, digits)-> np.ndarray:
        result = np.zeros(clusters.shape[0])

        return result



