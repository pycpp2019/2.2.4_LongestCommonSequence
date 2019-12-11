import numpy as np

# Longest common sequence - Brute-force
def lcs_bf(x, y):
    if len(x) == 0 or len(y) == 0:
        return np.array([])
    if x[-1] == y[-1]:
        return np.append(lcs_bf(x[:-1], y[:-1]), x[-1])
    else:
        left = lcs_bf(x[:-1], y)
        right = lcs_bf(x, y[:-1])
        return left if len(left) > len(right) else right

# Longest common sequence - Dynamic programming
def lcs(x, y):
    L = np.zeros((len(x)+1, len(y)+1), dtype=np.int)
    for x_i, x_elem in enumerate(x):
        for y_i, y_elem in enumerate(y):
            if x_elem == y_elem:
                L[x_i][y_i] = L[x_i-1][y_i-1] + 1
            else:
                L[x_i][y_i] = max((L[x_i][y_i-1],L[x_i-1][y_i]))

    LCS = np.array([], dtype=np.int)
    x_i, y_i = len(x)-1, len(y)-1
    while x_i >= 0 and y_i >= 0:
        if x[x_i] == y[y_i]:
            LCS = np.append(LCS, x[x_i])
            x_i, y_i = x_i-1, y_i-1
        elif L[x_i-1][y_i] > L[x_i][y_i-1]:
            x_i -= 1
        else:
            y_i -= 1
    return np.flip(LCS, axis=0)
