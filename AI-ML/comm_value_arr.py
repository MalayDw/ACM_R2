#finds common value between arrays
import numpy as np
ar1 = np.random.randint(10,size=(3,3))
ar2 = np.random.randint(10,size=(3,3))
print("array 1 is: ", ar1)
print("array 2 is: ", ar2) 

cv=np.intersect1d(ar1, ar2)
print("common values between the two arrays: ",cv)