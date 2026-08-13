import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
x = np.array ( [ [1], [2], [3], [4], [5] ])
y = np.array ([ 20, 30, 40, 50, 60 ])
model = LinearRegression()
model.fit (x,  y)
predictions = model.predict(x)
mae = mean_absolute_error(y, predictions)
print(predictions)
print(mae)
