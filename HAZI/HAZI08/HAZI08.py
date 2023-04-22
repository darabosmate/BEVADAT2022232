import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error

#1
def load_iris_data() : #-> sklearn.utils.Bunch, -> sklearn.utils._bunch.Bunch
    iris = load_iris()
    return iris

#2
def check_data(iris)-> pd.core.frame.DataFrame:
    df = pd.DataFrame(iris.data) #, columns=[iris['sepal length (cm)', 'sepal width (cm)']]
    df.columns = iris.feature_names
    return df.iloc[:, :2].head(5)

#3
def linear_train_data(input)-> (np.ndarray, np.ndarray):
    df = pd.DataFrame(input.data) #, columns=[iris['sepal length (cm)', 'sepal width (cm)']]
    df.columns = input.feature_names
    df.drop(columns=['petal length (cm)', 'petal width (cm)'], inplace=True)
    
    return (df.iloc[:, 0].to_numpy(), df.iloc[:, 1].to_numpy())

#4
def logistic_train_data(input)-> (np.ndarray, np.ndarray):
    df_features = pd.DataFrame(input.data).iloc[:, :2]
    df_features.columns = input.feature_names[:2]
    df_target = pd.DataFrame(input.target)
    df_target.columns = ['target']
    df = pd.concat([df_features, df_target], axis=1)
    df = df[df.target < 2]
    
    return df.loc[:, ['sepal length (cm)', 'sepal width (cm)']].to_numpy(), df.loc[:, 'target'].to_numpy()

#5
def split_data(X, y):
    #X = X.sample(frac=1, random_state=42)
    np.random.seed()
    np.random.shuffle(X)
    np.random.shuffle(y)
    test_ratio = 0.2
    test_size = int(np.shape(X)[0] * test_ratio)
    X_test, X_train = X[:test_size], X[test_size:]
    y_test, y_train = y[:test_size], y[test_size:]


    return X_train, X_test, y_train, y_test

#6
def train_linear_regression(X_train, y_train):
    lin_reg = LinearRegression().fit(X_train, y_train)
    return lin_reg

#7
def train_logistic_regression(X_train, y_train):
    log_reg = LogisticRegression().fit(X_train, y_train)
    return log_reg

#8
#model: LogisticRegression
def predict(model, X_test)-> np.ndarray:
    y_pred = model.predict(X_test)
    return y_pred

#9
def plot_actual_vs_predicted(y_test, y_pred):
    fig, ax = plt.subplots()

    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.set_title('Actual vs Predicted Target Values')

    #fig.scatter(y_test, y_pred)
    #ax.plot(y_test, y_pred)
    ax.scatter(y_test, y_pred)
    return fig

#10
def evaluate_model(y_test, y_pred):
    squared_errors = [(yt - yp) ** 2 for yt, yp in zip(y_test, y_pred)]
    mse = sum(squared_errors) / len(y_test)
    return mse



