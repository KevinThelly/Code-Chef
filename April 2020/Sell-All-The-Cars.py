import numpy
T=int(input())
for i in range(T):
  N=int(input())
  A=list(map(lambda x:int(x),input().split()))
  A.sort()
  A=A[::-1]
  value=0
  for i in range(len(A)):
    k=A[i]-i
    if(k>0):
      value=value+k
  print(value%1000000007)

  