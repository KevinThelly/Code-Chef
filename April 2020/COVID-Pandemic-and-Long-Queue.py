T=int(input())
for i in range(T):
  N=int(input())
  A=list(map(lambda x:int(x),input().split()))
  prev=A.index(1)
  val=0
  for i in range(prev+1,len(A)):
    if(A[i]==1):
      if(i-prev<6):
        val=1
        break
      prev=i
  if(val==1):
    print("NO")
  else:
    print("YES")
    