from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array ([[1], [2], [3], [4], [5]])
y = np.array ([[28], [30], [31], [33], [35]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ( [[6] ] )
print(prediction)

