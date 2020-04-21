
t = int(input())
for i in range(t):
  n=list(map(int,input().split()))
  a=list(map(int,input().split()))

  total=sum(a)
  result=total%n[1]

  print(result)
