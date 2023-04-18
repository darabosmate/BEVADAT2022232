import numpy as np




class LinearRegression:


    def __init__(self, epochs: int = 1000, lr: float = 1e-3):


        self.epochs = epochs
        self.lr = lr
        



    def fit(self, X: np.array, y: np.array):


        self.X_train = X


        self.Y_train = y



        self.m = 0


        self.c = 0


        epochs = 1000  # The number of iterations to perform gradient descent



        n = float(len(self.X_train)) # Number of elements in X



        losses = []


        for i in range(epochs): 


            y_pred = self.m*self.X_train + self.c  # The current predicted value of Y



            residuals = self.Y_train - y_pred


            loss = np.sum(residuals ** 2)
            losses.append(loss)


            D_m = (-2/n) * sum(self.X_train * residuals)  # Derivative wrt m


            D_c = (-2/n) * sum(residuals)  # Derivative wrt c


            self.m = self.m - self.lr * D_m  # Update m


            self.c = self.c - self.lr * D_c  # Update c


            if i % 100 == 0:


                print(np.mean(self.Y_train - y_pred))



    def predict(self, X):
        self.X_test = X
        pred = []
        for X in self.X_test:
            y_pred = self.m*X + self.c
            pred.append(y_pred)
        return pred


