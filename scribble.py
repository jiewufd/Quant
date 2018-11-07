import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = -np.arange(100)
y = np.random.rand(100)
line = plt.plot(x,y)
plt.xticks([0,40,60,80])
plt.legend([line],["line"])
plt.show()