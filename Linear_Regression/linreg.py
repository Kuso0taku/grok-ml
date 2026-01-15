# to generate random k, b
from random import random, randint

# class with different types of Linear Regression 
class Linear_regression:
    # init class
    def __init__ (self, rate=0.1, method=2):
        self.rate = rate
        self.method = method

    # Simple method (note that here's rate1 == rate2 so it's just rate)
    def _simple_trick(self, price_per_room, base_price, rooms, price):
        predicted_price = price_per_room * rooms + base_price
        if rooms > 0 and price > predicted_price:
            price_per_room += self.rate # or rate1
            base_price += self.rate # or rate2
        elif rooms > 0 and price < predicted_price:
            price_per_room -= self.rate 
            base_price -= self.rate 
        elif rooms < 0 and price > predicted_price:
            price_per_room -= self.rate 
            base_price += self.rate
        elif rooms < 0 and price < predicted_price:
            price_per_room += self.rate 
            base_price -= self.rate
        return price_per_room, base_price

    # Quadratic method 
    def _quad_trick(self, price_per_room, base_price, rooms, price):
        predicted_price = price_per_room * rooms + base_price
        price_per_room += self.rate * rooms * (price - predicted_price)
        base_price += self.rate * (price - predicted_price)
        return price_per_room, base_price

    # Absolute method
    def _absolute_trick(self, price_per_room, base_price, rooms, price):
        predicted_price = price_per_room * rooms + base_price
        if price > predicted_price:
            price_per_room += self.rate * rooms 
            base_price += self.rate 
        else:
            price_per_room -= self.rate * rooms 
            base_price -= self.rate 
        return price_per_room, base_price

    # linear regression
    def fit(self, features, labels, epochs=10000):
        self.price_per_room = random()
        self.base_price = random()

        if self.method == 0: trick = self._simple_trick
        elif self.method == 1: trick = self._quad_trick
        elif self.method == 2: trick = self._absolute_trick

        for epoch in range(epochs):
            i = randint(0, len(features)-1)
            rooms = features[i]
            price = labels[i]
            self.price_per_room, self.base_price = trick(
                    self.price_per_room, self.base_price, rooms, price)
        return self

    # prediction
    def predict(self, rooms):
        return self.price_per_room * rooms + self.base_price

    # get parameters
    def get_params(self):
        return self.price_per_room, self.base_price
