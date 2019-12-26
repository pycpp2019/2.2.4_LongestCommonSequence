import numpy as np

# Longest common sequence - Brute-force
def lcs_bf(a, b):
    if len(a) * len(b) == 0:
        return np.array([])
    if a[-1] == b[-1]:
        return np.append(lcs_bf(a[:-1], b[:-1]), a[-1])
    else:
        left = lcs_bf(a[:-1], b)
        right = lcs_bf(a, b[:-1])
        if len(left) > len(right):
            return left
        else:
            return right

# Longest common sequence - Dynamic programming
def fill_dyn_matrix(x, y):
    L = [[0]*(len(y)+1) for _ in range(len(x)+1)]
    for x_i, x_elem in enumerate(x):
        for y_i, y_elem in enumerate(y):
            if x_elem == y_elem:
                L[x_i][y_i] = L[x_i-1][y_i-1] + 1
            else:
                L[x_i][y_i] = max((L[x_i][y_i-1],L[x_i-1][y_i]))
    return L

def lcs(x, y):
    L = fill_dyn_matrix(x, y)
    LCS = []
    x_i, y_i = len(x)-1, len(y)-1
    while x_i >= 0 and y_i >= 0:
        if x[x_i] == y[y_i]:
            LCS.append(x[x_i])
            x_i, y_i = x_i-1, y_i-1
        elif L[x_i-1][y_i] > L[x_i][y_i-1]:
            x_i -= 1
        else:
            y_i -= 1
    LCS.reverse()
    return np.array(LCS)