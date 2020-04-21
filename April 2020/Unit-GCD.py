T=int(input())

for i in range(T):
  N=int(input())

  i=1
  if(N==0):
    print(0)
    continue
  elif(N==1):
    print(1)
    print(1,1)
  elif(N==2):
    print(1)
    print(2,1,2)
  elif(N==3):
    print(1)
    print(3,1,2,3)
  else:
    print(N//2)
  a=[]
  if(N>3):
    print(3,1,2,3)
    i=4
    while(i<N):
      print(2,i,i+1)
      i=i+2

    if(i==N):
      print(1,N)
  