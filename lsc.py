import numpy as np
def lcs_bf(x,y):
  m=0
  ans=[]
  xS=[]
  yS=[]
  for i in range(len(y)):
    for j in range(i+1,len(y)):
      yS.append(y[i:j])
    yS.append(y[i:])
  for i in range(len(x)):
    for j in range(i+1,len(x)):
      xS.append(x[i:j])
    xS.append(x[i:])
  for i in xS:
    if i in yS and len(i)>len(ans):
      ans=i
  return np.array(ans)


def lcs(x,y):
  lcs=np.zeros(len(x)*len(y),dtype=int).reshape(len(x),len(y))
  prevI=np.zeros(len(x)*len(y),dtype=int).reshape(len(x),len(y))
  prevJ=np.zeros(len(x)*len(y),dtype=int).reshape(len(x),len(y))
  for i in range(1,len(x)):
    for j in range(1,len(y)):
      if x[i] == y[j]:
        lcs[i][j] = lcs[i-1][j-1] + 1
        prevI[i][j] = i-1
        prevJ[i][j] = j-1
      else:
        if lcs[i-1][j] >= lcs[i][j-1]:
          lcs[i][j] = lcs[i-1][j]
          prevI[i][j] = i-1
          prevJ[i][j] = j
        else:
          lcs[i][j] = lcs[i][j-1]
          prevI[i][j] = i
          prevJ[i][j] = j-1
  ans=[]
  takeLCS(len(x)-1,len(y)-1,x,y,prevI, prevJ,ans)
  return ans

def takeLCS(i,j,x,y,prevI,prevJ,ans):
  if i == 0 or j == 0:
    if x[i]==y[j]:
      ans.append(x[i])
    return np.array(ans.reverse())
  if (prevI[i][j] == i-1) and (prevJ[i][j] == j - 1): 
    ans.append(x[i])
    takeLCS(i - 1, j - 1,x,y,prevI,prevJ,ans)
   
  else:
    if prevI[i][j] == i - 1 and prevJ[i][j] == j:
      takeLCS(i - 1, j,x,y,prevI,prevJ,ans)
    else:
      takeLCS(i, j - 1,x,y,prevI,prevJ,ans)