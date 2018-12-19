""" Portable Linear Regression Module - MSE """

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
        self.m = self.fileSize[0]
        self.featureSize = self.fileSize[1]-1
        if self.featureSize >= 10:
            print("So many features? Beware of overfitting")
        self.x = self.file[:,:self.featureSize]
        self.y = self.file[:,-1]
        self.X = np.c_[np.ones(self.m), self.x]
        self.Theta = np.zeros(self.featureSize+1)
        self.Cost = []
        self.mean = self.x.mean()
        self.sigma = self.x.std()


    def visualizedata(self, xlabel="X", ylabel="Y", Predict=None, Cost=False):
        """
        Plot the Initial Data and Prediction
        """
        plt.figure()

        for i in range(self.featureSize):
            plt.subplot(self.featureSize, 1, i+1)
            plt.plot(self.x[:,i], self.y, 'x')
            if Cost == True:
                plt.plot(self.x[:,i], self.Cost[-1])

            if Predict != None:
                _Predict = self.featureStandardize(Predict)
                plt.plot(Predict, _Predict @ self.Theta, 'o')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()


    def featureStandardize(self, Features=None):
        """ Standardize data to ease GD process """
        if Features == None:
            self.X = np.c_[np.ones(self.m), np.divide((self.x - self.mean), self.sigma)]
            return self.X
        else:
            X = np.asarray(Features)
            X = np.c_[np.ones(X.shape[0]), np.divide((X.copy() - self.mean), self.sigma)]
            return X


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


    def gradientDescent(self, LearningRate, Epoch):
        """
        Finds the minima of a curve
        Aserguments:
            - Learning Rate
            - Epoch : Number of iteration
        """
        for i in range(Epoch):
            _h = self.X @ self.Theta - self.y

            for j in range(self.featureSize+1):
                self.Theta[j] = self.Theta[j] - (LearningRate/self.m) * (_h.T @ self.X[:, j])
            self.Cost.append(self.X @ self.Theta)
        return self.Theta

    def table(self):
        """ Prints out First 10 initial data """
        labels = 'X'*self.featureSize + 'Y'
        return pd.DataFrame(self.file[:10, :], columns=list(labels))



if __name__ == "__main__":
    while True:
        LearningRate = Epoch = None
        filename = input('Input file name: \'eg1\' / \'eg2\'\n')
        if filename == 'eg1':
            filename, LearningRate, Epoch = 'ex1data1.txt', 0.01, 1000
        elif filename == 'eg2':
            filename, LearningRate, Epoch = 'ex1data2.txt', 0.01, 1000
        elif not filename.endswith(('.txt','.csv')):
            print("No .txt or .csv file detected")
            continue

        data = Linear_Regression(filename)
        print(f'\nFirst 10 initial data samples \n\n{data.table()}\n')
        data.visualizedata()
        print(f'\nCost BEFORE Gradient Descent is {data.computeCost()} \n\nInitializing Feature Standardization...\n')
        data.featureStandardize()
        print("Initializing Gradient Descent... \n")

        if LearningRate is None:
            LearningRate = float(input("Input Learning rate: "))
            Epoch = int(input("Input Epoch(iterations): "))
        data.gradientDescent(LearningRate, Epoch)
        print(f'\nCost AFTER Gradient Descent {data.computeCost()}\n')

        if filename == 'ex1data1.txt':
            data.visualizedata(xlabel='Population of City in 10,000s', ylabel='Profit in $10,000s', Predict=[11,19,15,25], Cost=True)
        elif filename == 'ex1data2.txt':
            data.visualizedata(xlabel='House Size sq/ft', ylabel='Price', Predict=[[6800,4],[4400,3]], Cost=True)


        print('The End')
