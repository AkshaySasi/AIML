import numpy as np

class NaiveBayes:

    def fit(self, X, y):
        n_smaples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        #calculate mean, var and prior for each class
        self._mean = np.zeros()


    def predict()    