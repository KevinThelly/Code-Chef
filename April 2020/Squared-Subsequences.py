def twos(a):
  count=0
  if(a==0):
    return 0
  while(a%2==0):
    a=a/2
    count+=1
  return count

T=int(input())
for i in range(T):
  N=int(input())
  A=list(map(lambda x: int(x),input().split()))
  result=N*(N+1)/2
  odd=0
  i=0

  while(i<len(A)):

    if(A[i]%2==1):
      odd+=1
      i+=1
      # print("2")
    elif(twos(A[i])==1):
      result=result-1-odd
      i+=1
      if(i<len(A) and A[i]%2==0):
        odd=0
      odd2=0
      # print("3")
      while(i<len(A) and A[i]%2==1):
        result=result-1-odd
        odd2+=1
        i+=1
        # print("3 :",odd2)
        if(i<len(A) and twos(A[i])==1):
          odd=odd2
    else:
      odd=0
      i+=1
      # print("4")
  
  print(int(result))

