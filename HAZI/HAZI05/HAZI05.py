

import numpy as np

import seaborn as sns

from typing import Tuple

from scipy.stats import mode

from sklearn.metrics import confusion_matrix
import pandas as pd



class KNNClassifier:


    @property

    def k_neighbors(self):

        return self.k


    def __init__(self, k: int, test_split_ratio: float) -> None:

        self.k = k
        self.test_split_ratio = test_split_ratio


        self.x_test, self.y_test = None, None

        self.x_train, self.y_train = None, None

        self.y_preds = None


    def train_test_split(self, features: pd.DataFrame, labels: pd.DataFrame) -> None:

        test_size = int(features.shape[0] * self.test_split_ratio)

        train_size = features.shape[0] - test_size

        assert features.shape[0] == test_size + train_size, "Size mismatch!"


        self.x_train, self.y_train = features.iloc[:train_size, :], labels.iloc[:train_size]

        self.x_test, self.y_test = features.iloc[train_size:train_size+test_size, :], labels.iloc[train_size:train_size + test_size]


    def euclidean(self, element_of_x: pd.DataFrame) -> pd.DataFrame:

        return np.sqrt(np.sum((self.x_train - element_of_x)**2, axis=1))


    def predict(self, x_test: pd.DataFrame) -> None:

        labels_pred = []

        for idx, x_test_element in x_test.iterrows():

            distances = self.euclidean(x_test[idx, :])

            distances = np.array(sorted(zip(distances, self.y_train))) #######TODO

            label_pred = mode(distances[:self.k, 1], keepdims=False).mode

            labels_pred.append(label_pred)

        self.y_preds = pd.DataFrame(labels_pred)


    def accuracy(self) -> float:
        true_positive = (self.y_test == pd.DataFrame(self.y_preds)).sum()

        return true_positive / self.y_test.shape[0] * 100


    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)

        return conf_matrix


    @staticmethod

    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        df = pd.read_csv(csv_path)
        df = df.sample(frac=1, random_state=42, ignore_index=True)
        x_ = df.iloc[:, :8]
        y_ = pd.DataFrame(df['Outcome'])

        return x_, y_