
t = int(input())
for i in range(t):
  n=int(input())
  
  a=list(map(int,input().split()))
  a=sorted(a)

  b=list(map(int,input().split()))
  b=sorted(b)

  s=0
  for i in range(n):
    if(a[i]<b[i]):
      s=s+a[i]
    else:
      s=s+b[i]
  
  print(s)