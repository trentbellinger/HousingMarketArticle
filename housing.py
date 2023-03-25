import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn import svm

supply = np.array([106.28,112.66,119.63,123.93,130.6,132.29,132.78,132.8,133.27,134.7,135.58,136.57,138.45,139.64,140.8,141.95])
population = np.array([248.08,265.66,282.4,296.84,311.18,313.88,316.65,319.4,322.03,324.61,327.21,329.8,332.14,334.32,335.94,337])
indexes = np.array([71.86, 67.84, 79.92, 117.14, 82.58, 78.34, 81.23, 88.2, 91.94, 95.34, 98, 101.9, 104.44, 106, 115.37, 129.06])
housingPerCapita = np.array([166.3, 191.43, 241.84, 354.9, 324.13, 313.34, 315.22, 328.89, 345.71, 363.17, 383, 403.87, 423.66, 444.99, 472.69, 558.11])
time = np.array([1990,1995,2000,2005,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])

for i in range(0,len(supply)):
  housingPerCapita[i] = (supply[i]/population[i])
  housingPerCapita[i] = housingPerCapita[i]*200  #Adjust for graphing
X_train, X_test, y_train, y_test = train_test_split(housingPerCapita, indexes, test_size = 0.20, random_state = 53)



plt.figure()
plt.plot(time, indexes)
plt.plot(time, housingPerCapita)
plt.xlabel("Year")
plt.ylabel("Inflation-Adjusted Housing Price Index")
plt.legend(["Inflation-Adjusted Housing Price Index", "Adjusted Housing Supply Per Capita"])
plt.figure()
plt.scatter(housingPerCapita, indexes)
plt.xlabel("Adjusted Housing Supply Per Capita")
plt.ylabel("Inflation-Adjusted Housing Price Index")
a = np.polyfit(housingPerCapita, indexes, 1)
plt.plot(housingPerCapita, np.multiply(a[0],housingPerCapita) + a[1], c="green", label="Line of best fit")
plt.legend()
print("Correlation coefficient: ", np.corrcoef(housingPerCapita, indexes)[1][0])