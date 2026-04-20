import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('data/cleaned_air_quality.csv')
df['Year'] = pd.to_datetime(df['Start_Date']).dt.year
df = df.drop(columns=['Start_Date', 'Period'])
df = pd.get_dummies(df, columns=['Pollutant', 'Location', 'Measure', 'Measure Info'], drop_first=True)

X = df.drop(columns=['Value'])
y = df['Value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Model trained. RMSE: {rmse:.2f}")
