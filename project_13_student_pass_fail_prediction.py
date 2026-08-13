from sklearn.linear_model import LogisticRegression
import numpy as np
x = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array ([0,   0,   0,   0,   1,  1,  1,  1,])
model = LogisticRegression()
model.fit (x, y)
prediction = model.predict ([ [6] ] )
print(prediction)
if prediction [0] == 1:
	print("Result:  PASS")
else:
	    print("Result: FAIL")

