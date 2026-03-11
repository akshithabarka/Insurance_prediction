#1.Load the scaled or processed data from processed folder
#2.Create model and scale data
#3.Save model data into processed folder
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
X_train = pd.read_csv("../data/processed/X_train.csv")
X_test = pd.read_csv("../data/processed/X_test.csv")
y_train = pd.read_csv("../data/processed/y_train.csv")
y_test = pd.read_csv("../data/processed/y_test.csv")
print(X_train)

model = LinearRegression()
model.fit(X_train,y_train)

with open("../artifacts/model.pkl","wb") as f:
    pickle.dump(model,f)