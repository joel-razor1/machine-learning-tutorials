# Data Preprocessing

#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset

dataset=pd.read_csv('Data.csv')
X=dataset.iloc[: ,:-1].values
y=dataset.iloc[: , 3].values

#Taking care of the missing data

from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer=Imputer.fit(X[: , 1:3])

#Encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X=LabelEncoder()
X[:,0]=labelEncoder_X.fit_transform(X[:, 0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
labelEncoder_y=LabelEncoder()
y=labelEncoder_X.fit_transform(y)


#Splitting dataset into Training and test set

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=0)

#Feature Scaling

from sklearn.preprocessing import StandardScalar
sc_X=StandardScalar()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)