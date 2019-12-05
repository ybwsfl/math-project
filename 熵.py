import numpy as np

def calc_ent(x):
    """
        calculate shanno ent of x
    """

    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        logp = np.log2(p)
        ent -= p * logp

    return ent

np.random.rand(10)
np.random.randn(10)
np.random.randint(10,size=10)

arr = np.arange(10)
np.random.shuffle(arr)

np.random.permutation(10)

print(calc_ent(np.random.randn(10)))

print(np.random.random((3,3)))
print(np.random.random((3,3)).reshape(-1))