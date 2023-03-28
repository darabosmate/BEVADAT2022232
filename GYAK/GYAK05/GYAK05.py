
import numpy as np
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix


csv_path = "archive/iris.data.csv"

class KNNClassifier:

    k_neighbors = 0

    def __init__(self, k:int, test_split_ratio:float)-> None:
        self.k = k
        self.test_split_ratio = test_split_ratio
    
    def train_test_split(self, features:np.ndarray, labels:np.ndarray) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features[:train_size,:],labels[:train_size]
        self.x_test, self.y_test = features[train_size:train_size+test_size,:], labels[train_size:train_size + test_size]
        #return (x_train,y_train,x_test,y_test)  

    def euclidean(self, points:np.ndarray,element_of_x:np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum((points - element_of_x)**2,axis=1))





    @staticmethod
    def load_csv(csv_path:str) ->Tuple[np.ndarray,np.ndarray]:
        df = pd.read_csv("archive/iris.data.csv")
        df = df.sample(frac=1).reset_index(drop=True)
        x,y = dataset[:,:4],dataset[:,-1]
        return x,y
