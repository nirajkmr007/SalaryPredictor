'''
Created on Mar 16, 2018

@author: Mmk
'''
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def pridict_sal(    ):
    #username = request.args.get('exp')
    #print(username)
    dataset = pd.read_csv("Salary_Data.csv")
    X = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
    
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(1.5)
    
    return str(y_pred)

@app.route('/my_endpoint/<int:id>', methods=['GET'])
def my_endpoint_handler(id):
    print(id)
    dataset = pd.read_csv("Salary_Data.csv")
    X = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
    
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(int(id))
    
    return str(y_pred*15)

if __name__ == '__main__':
    print(pridict_sal())
    app.run(debug=True)
