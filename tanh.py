import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100,100,100)

y = np.tanh(x)

plt.plot(x,y,label="label",color="red",linewidth=2)

plt.xlabel("abscissa")

plt.ylabel("ordinate")

plt.title("tanh example")

plt.show()