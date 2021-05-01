from flask import Flask, request, render_template

#Import libraries
import pandas as pd
import numpy as np

#Import ML package
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():

    #Prep data
    dataset = pd.read_csv("startup_data.csv")
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1:].values

    #Train the algorithm
    regressor = RandomForestClassifier(n_estimators=50, random_state=0)
    regressor.fit(x, y)

    #Getting input data

    if request.method == 'POST':
        funding = request.form.get('funding')
        rounds = request.form.get('rounds')
        values = ([[funding, rounds]])
        result = regressor.predict(values)[0]
        if result == 1:
            output = "Get on this rocketship. THIS STARTUP IS GOING TO THE MOON!"
        else:
            output = "It's unlikely this startup will succeed."
    return output #render_template("index.html", prediction_text = output)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)