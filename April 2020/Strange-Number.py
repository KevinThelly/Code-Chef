import math
def primeFactors(n): 
  a=[]

  while n % 2 == 0: 
    a.append(2) 
    n = n / 2
 
  for i in range(3,int(math.sqrt(n))+1,2): 
    while n % i== 0: 
      a.append(i)
      n = n / i 
           
  if n > 2: 
    a.append(n)
  return(a)



T=int(input())
for i in range(T):
  X,K=map(lambda x: int(x),input().split())
  primes=primeFactors(X)
  if(K<=len(primes)):
    print(1)
  else:
    print(0)
