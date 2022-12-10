import numpy as np
cart=np.random.random((10,2)).round(3)*10
print("cartesian coordinates: ", cart)
l=[]
for i in cart:
    r=np.sqrt(i[0]**2 + i[1]**2)
    if i[0]==0:
        tan=np.inf
    else:
        tan=i[1]/i[0]
    theta=np.arctan(tan)
    l.append((r,theta))
polar=np.array(l)
print("converted polar coordinates: ", polar)