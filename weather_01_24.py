import pandas as pd
import datetime
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression

#import the csv file
df = pd.read_csv('charlotte.csv')

#fill all blank rows
df = df.fillna(method = 'ffill')

df.describe()
#convert kelvin to F
df['temperature']=(df['temperature']-273.15)*9/5+32
x = df.iloc[:,0:6].values
y = df.iloc[:,6].values

labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])
x[:,5] = labelencoder_x.fit_transform(x[:,5])

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 0)


#Feature Scaling using Standard Sclaer#Feature 
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler() 
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

y_pred = lin_reg.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
cm