#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Linear_Regression:
    """
    # MACHINE LEARNING - Linear Regression (1 Output only)
    #
    # Purpose:  To predict future outcome when there's a linear relationship.
    #           (eg. The relationship of a Student's study hours and his/her Exam Score.)
    # Method:   Compute Cost using 'Mean Squared Error'
    # Inputs:   Any text files with CVS format, having 1 or more features with the outcome as the last column value.
    """
    def __init__(self, filename):
        """ Initialize """
        if filename.endswith(('.txt','.csv')):
            self.file = np.loadtxt(filename, delimiter= ',')
        else:
            raise ValueError("No .txt or .csv file detected")
        self.fileSize = self.file.shape
        self.featureSize = self.fileSize[1]-1
        if self.featureSize >= 10:
            print("So many features? Beware of overfitting")
        self.m = self.fileSize[0]
        self.x = self.file[:,:self.featureSize]
        self.y = self.file[:,-1]
        self.X = np.c_[np.ones(self.m), self.x]
        self.Theta = np.zeros(self.featureSize+1)
        self.Cost = []

    def visualizedata(self):
        """ plot the given raw data """
        plt.plot(self.x, self.y, 'bo')
        plt.show()
        return

    def computeCost(self):
        """
        Computes the Mean Squared Error of given data.
        Cost hypothesis:

            Y = Theta[0]+Theta[n]*Feature

        - theta are weights
        """
        h = self.X @ self.Theta - self.y

        J = (h.T @ h)/(2*self.m)
        return J

    def gradientDescent(self, Alpha, Epoch):
        """
        Finds the minima of a curve
        Aserguments:
            - Alpha : Learning rate
            - Epoch : Number of iteration
        """
        plt.figure()
        for i in range(Epoch):
            _h = self.X @ self.Theta - self.y

            for j in range(self.featureSize+1):
                self.Theta[j] = self.Theta[j] - (Alpha/self.m) * (_h.T @ self.X[:,j])
            self.Cost.append(self.X @ self.Theta)
        plt.plot(self.x, self.Cost[i])
        print(f'Theta/weights = {self.Theta}')
        self.visualizedata()
        return self.Theta

    def table(self):
        _list = 'X'*self.featureSize + 'Y'
        return pd.DataFrame(self.file[:10,:], columns=list(_list))


if __name__ == "__main__":
    while True:
        Alpha = Epoch = None
        filename = input('Enter file name, \'eg\', or \'.\' to quit: \n')
        if filename == 'eg':
            filename, Alpha, Epoch = 'ex1data1.txt', 0.01, 1500
        elif filename == '.':
            break
        elif not filename.endswith(('.txt','.csv')):
            print("No .txt or .csv file detected")
            continue
        data = Linear_Regression(filename)
        print(f'10 Initial data samples \n \n {data.table()} \n')
        data.visualizedata()
        print(f'Cost BEFORE Gradient Descent {data.computeCost()}')
        print("Initializing Gradient Descent \n")
        if Alpha is None:
            Alpha = float(input("Input Alpha(learning rate): "))
            Epoch = int(input("Input Epoch(iterations): "))
        data.gradientDescent(Alpha, Epoch)
        print(f'Cost AFTER Gradient Descent {data.computeCost()}')
