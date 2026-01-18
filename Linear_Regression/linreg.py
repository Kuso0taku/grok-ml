# to generate random k, b
from random import random, randint
from numpy import dot

# class with different types of Linear Regression 
class Linear_regression:
    # init class
    def __init__ (self, rate=0.1, method=2):
        self.rate = rate
        self.method = method
        self.W = None
        self.b = None

    # Simple method
    def _simple_trick(self, features, label):
        y_hat = dot(self.W, features) + self.b
        
        if label > y_hat:
            self.b += self.rate 
            for i in range(len(features)):
                if features[i] > 0:
                    self.W[i] += self.rate
                else:
                    self.W[i] -= self.rate
        else:
            self.b -= self.rate
            for i in range(len(features)):
                if features[i] > 0:
                    self.W[i] -= self.rate
                else:
                    self.W[i] += self.rate

        return self.W, self.b

    # Quadratic method 
    def _quad_trick(self, features, label):
        y_hat = dot(self.W, features) + self.b
        diff = label - y_hat 

        self.b += self.rate * diff 
        for i in range(len(features)):
            self.W[i] += self.rate * features[i] * diff

        return self.W, self.b

    # Absolute method
    def _absolute_trick(self, features, label):
        y_hat = dot(self.W, features) + self.b

        if label > y_hat:
            self.b += self.rate
            for i in range(len(features)):
                self.W[i] += self.rate * features[i]
        else:
            self.b -= self.rate
            for i in range(len(features)):
                self.W[i] -= self.rate * features[i]

        return self.W, self.b

    # linear regression
    def fit(self, features, labels, epochs=10000):
        self.b = random()
        self.W = [random() for _ in features[0]]

        if self.method == 0: trick = self._simple_trick
        elif self.method == 1: trick = self._quad_trick
        elif self.method == 2: trick = self._absolute_trick

        for epoch in range(epochs):
            i = randint(0, len(features)-1)
            X = features[i]
            y = labels[i]

            trick(X, y)

        return self

    # prediction
    def predict(self, features):
        return dot(self.W, features) + self.b

    # get parameters
    def get_params(self):
        return self.W, self.b
