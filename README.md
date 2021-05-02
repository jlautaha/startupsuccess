# Startup Success

**Link to app:** [https://startup-success-312408.uk.r.appspot.com](https://startup-success-312408.uk.r.appspot.com)

**Link to video demo:**

**Linked to Kaggle dataset:** I used [this Kaggle dataset](https://www.kaggle.com/manishkc06/startup-success-prediction), but edited the CSV to only keep the columns funding_rounds, funding_total_usd, and status, and rename them rounds, funding and status.

**Description:** This project predicts the success of a startup based on the amount of funding its received and the number of rounds of funding it's passed. Success is defined as acheiving an exit through acquisition or IPO.

---

## **Framework:**
![Framework](https://raw.githubusercontent.com/jlautaha/startupsuccess/main/framework%20pic%20v2.PNG)

---

## **Building the Model:**

1. Import libraries

```
import pandas as pd
import numpy as np
```

2. Read dataset

```
dataset = pd.read_csv("startup_data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1:].values
```

3. Divide dataset into training and testing

```
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
```

4. Train the algorithm

```
from sklearn.ensemble import RandomForestClassifier
regressor = RandomForestClassifier(n_estimators=50, random_state=0)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
```

5. Evaluate the algorithm

```
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
```

Output:

![output](https://raw.githubusercontent.com/jlautaha/startupsuccess/main/model%20evaluation.PNG)

**Note:** This is not the most precise model and I split the dataset to train and evaluate the model. However, I eventually used _the entire dataset_ to train the final model as seen below.

---

## **Building and Deploying Flask app with the model:**

As I mentioned above, when building the model within the Flask app, I trained on the entire dataset to hopefully get a more precise model.

```
regressor = RandomForestClassifier(n_estimators=50, random_state=0)
    regressor.fit(x, y)
```

I then took user inputs from the app, put it in array form in order to run a prediction, and return the prediction.

```
    if request.method == 'POST':
        funding = request.form.get('funding')
        rounds = request.form.get('rounds')
        values = ([[funding, rounds]])
        result = regressor.predict(values)[0]
    return render_template("results.html", prediction = result)
 ```
 
 I then create, build and deploy through Google CLI. [Here](https://startup-success-312408.uk.r.appspot.com) is the resulting URL and below is the interface:
 
 ![interface](https://raw.githubusercontent.com/jlautaha/startupsuccess/main/screenshot1.PNG)
 
 Here's an example of predicting success:
 
 ![successprediction](https://raw.githubusercontent.com/jlautaha/startupsuccess/main/screenshot2.PNG)
 
 Here's an example of predicting failure:
 
 ![failureprediction](https://raw.githubusercontent.com/jlautaha/startupsuccess/main/screenshot3.PNG)
 
 ---
 
 ## **Building Continuous Deployment:**
 
 Follow [these steps](https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories#before-you-begin) in order to build continuous deployment in Google Cloud.
 
 Below shows trigger history indicating updates into our app.
 
 ![tiggerpush](https://raw.githubusercontent.com/jlautaha/startupsuccess/main/push%20trigger.PNG)
 
 ---
 
  ## **Thanks for checking this out!**
 
 
 
 
