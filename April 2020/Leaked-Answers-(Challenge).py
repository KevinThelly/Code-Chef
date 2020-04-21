def count(a,m):
  maximum=0
  num=1
  for i in range(1,m+1):
    b=a.count(i)
    if(b>maximum):
      maximum=b
      num=i
  return num


T=int(input())
for i in range(T):
  N,M,K=list(map(lambda x: int(x),input().split()))
  a=[]
  for i in range(N):
    a.append(list(map(lambda x:int(x),input().split())))
  for i in a:
    print(count(i,M),end=" ")
  print()
      


