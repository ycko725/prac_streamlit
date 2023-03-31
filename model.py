
import pandas as pd 

from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("data/iris.csv")

le = LabelBinarizer()

data['species'] = le.fit_transform(data['species'])

X = data.drop(columns=['species'])
y = data['species']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = LogisticRegression()
model.fit(X_train, y_train) 

model_file = open("models/lgr_model_iris230331.pkl", "wb")
joblib.dump(model, model_file) 
model_file.close() 