import numpy as np
from func import func1, func2
# import pandas as pd
# import matplotlib.pyplot as plt
from datetime import datetime
                        # Max Limit 10000000
a = np.random.randint(100, size = 1000)  
# print(a)
# a = 1000000
t0 = datetime.now() 
result1 = func1(a)
dt1 = datetime.now() - t0

t0 = datetime.now()
result2 = func2(a)
dt2 = datetime.now() - t0
print(result1)
print(result2)
print('dt1 -> ', dt1.total_seconds())
print('dt2 -> ', dt2.total_seconds())