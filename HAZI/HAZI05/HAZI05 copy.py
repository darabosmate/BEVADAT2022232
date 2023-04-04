

import numpy as np

import seaborn as sns

from typing import Tuple

from scipy.stats import mode

from sklearn.metrics import confusion_matrix
import pandas as pd


class KNNClassifier:

    @property
    def k_neighbors(self):  # 1

        return self.k

    def __init__(self, k: int, test_split_ratio: float) -> None:

        self.k = k
        self.test_split_ratio = test_split_ratio

        self.x_test, self.y_test = None, None

        self.x_train, self.y_train = None, None

        self.y_preds = None

    def train_test_split(self, features: pd.DataFrame, labels: pd.DataFrame) -> None:  # 3

        test_size = int(features.shape[0] * self.test_split_ratio)

        train_size = features.shape[0] - test_size

        assert features.shape[0] == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features.iloc[:train_size,
                                                   :], labels.iloc[:train_size].reset_index(drop=True)

        self.x_test, self.y_test = features.iloc[train_size:train_size +
                                                 test_size, :], labels.iloc[train_size:train_size + test_size].reset_index(drop=True)

    def euclidean(self, element_of_x: pd.DataFrame) -> pd.DataFrame:  # 4

        return np.sqrt(np.sum((self.x_train - element_of_x)**2, axis=1))


    def predict(self,x_test:pd.DataFrame) -> pd.Series: #5
        labels_pred = []
        for idx, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.concat([distances, self.y_train], axis=1).sort_values(by=0)
            label_pred = mode(distances.iloc[:self.k,1],keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = pd.DataFrame(labels_pred)

    def accuracy(self) -> float:  # 6
        true_positive = (self.y_test.iloc[:, 0] == self.y_preds.iloc[:, 0]).sum()

        return true_positive / self.y_test.shape[0] * 100

    def confusion_matrix(self):  # 7
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)

        return conf_matrix

    def best_k(self):
        ret = tuple((1, -1))
        for i in range(1, 21):
            self.k = i
            self.predict(self.x_test)
            acc = self.accuracy()
            if acc > ret[1]:
                ret = (self.k, acc.round(2))

        return ret

    @staticmethod
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:  # 2
        df = pd.read_csv(csv_path)
        df = df.sample(frac=1, random_state=42, ignore_index=True)
        x_ = df.iloc[:, :-1]
        # pd.DataFrame(df['Outcome']) dupla [[]] = dataframet ad vissza series helyett
        y_ = pd.DataFrame(df.iloc[:, -1])

        return x_, y_
