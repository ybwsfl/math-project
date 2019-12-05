# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist


def sigmoid(x):
    return 1. / (1 + np.exp(-x))


def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def relu(x):
    return np.where(x < 0, 0, x)

def prelu(x):
    return np.where(0.5*x < 0, 0, x)

def plot_sigmoid():
    x = np.linspace(-100, 100, 1000)

    y = tanh(x)

    plt.plot(x, y, label="label", color="red", linewidth=2)

    plt.xlabel("abscissa")

    plt.ylabel("ordinate")

    plt.title("tanh example")

    plt.show()

if __name__ == "__main__":
    plot_sigmoid()
    # plot_tanh()
    # plot_relu()
            # plot_prelu()