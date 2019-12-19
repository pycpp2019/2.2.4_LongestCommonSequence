import numpy as np
def lcs_bf1(x,y):
  if len(x) == 0 or len(y) == 0:
    return []
  if x[-1] == y[-1]:
    return lcs_bf1(x[:-1], y[:-1]) + [x[-1]]
  else:
    l = lcs_bf1(x[:-1], y)
    r = lcs_bf1(x, y[:-1])
    if len(l) >= len(r):
      return l
    else:
      return r
def lcs_bf(x,y):
  return np.array(lcs_bf1(x,y))


def lcs(x,y):
  L = [[0]*(len(y)+1) for _ in range(len(x)+1)]
  for i,x_elem in enumerate(x):
    for j,y_elem in enumerate(y):
      if x_elem == y_elem:
        L[i][j] = L[i-1][j-1] + 1
      else:
        L[i][j] = max((L[i][j-1],L[i-1][j]))
  LCS = []
  i,j = len(x)-1,len(y)-1
  while i >= 0 and j >= 0:
    if x[i] == y[j]:
      LCS.append(x[i])
      i -= 1
      j -= 1
    elif L[i-1][j] > L[i][j-1]:
      i -= 1
    else:
      j -= 1
  LCS.reverse()
  return np.array(LCS)
#print(lcs([0, 5, 3, 9, 3, 3, 8, 4, 2, 5],[9, 0, 7, 6, 5, 0, 3, 7, 1, 0]))