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
  lcs=np.zeros(len(x)*len(y),dtype=int).reshape(len(x),len(y))
  for i in range(1,len(x)):
    for j in range(1,len(y)):
      if x[i] == y[j]:
        lcs[i][j] = lcs[i-1][j-1] + 1
      else:
        if lcs[i-1][j] >= lcs[i][j-1]:
          lcs[i][j] = lcs[i-1][j]
        else:
          lcs[i][j] = lcs[i][j-1]
  LCS = []
  i = len(x)-1
  j = len(y)-1
  while i >= 0 and j >= 0:
    if x[i] == y[j]:
      LCS.append(x[i])
      i -= 1
      j -= 1
    elif lcs[i-1][j] > lcs[i][j-1]:
      i -= 1
    else:
      j -= 1
  LCS.reverse()
  return np.array(LCS)
#print(lcs_bf([1,1,1,1],[2,1,2,1]))