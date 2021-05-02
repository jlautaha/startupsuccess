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


