def binary(n,length):
  sum=[]
  temp=n
  # print(temp)
  while(temp>0):
    if(temp%2==0):
      sum.append(0)
    else:
      sum.append(1)
    temp=temp//2
  sum=sum[::-1]  
  if(len(sum)<length):
    sum=[0]*(length-len(sum))+sum
#   return sum
# def binary(n,length):
#   sum=[0]*length
#   for i in range(n):
#     sum=[0]*length
#     for j in range(n):
#       sum[i:j]=[1]
#       print(sum)
#       bin.append(sum)
#   print(bin)

n=list(map(int,input().split()))
a=list(map(int,input().split()))
val=[]
l=[]
r=[]
for i in range(n[1]):
  q=list(map(int,input().split()))
  val.append(q[1]-q[0]+1)
  l.append(q[0]-1)
  r.append(q[1]-1)
# print("value ",val)

increase=0
decrease=0
flag=0

for i in range(len(val)):
  # bin=[]
  print("l,r",l[i],r[i])
  for j in range(1,2**int(val[i])):
    # bin.append(binary(j,int(val[i])))
    bin=binary(j,int(val[i]))
    p=bin.index(1) + l[i]
    pq=bin[::-1].index(1)
    pq=len(bin)-pq -1 + l[i]
    # print(bin,"p,q",p,pq)
    print("(p,q)",p,pq,end=" ")

    alpha=[]
    for k in range(len(bin)):
      if(bin[k]==1):
        alpha.append(a[l[i]+k])
        # print(alpha)

    # print(alpha,len(alpha))
    if(len(alpha)!=1):
      print(alpha)
      flag = all(i < j for i, j in zip(alpha, alpha[1:])) 
      if(flag):
        # print("increase")
        if(p==l[i] and pq==r[i]):
          print("increase1")
          increase=increase+1
        elif( (p>l[i] and a[p]<a[p-1]) and (pq<r[i] and a[pq]>a[pq+1])):
          increase=increase +1
          print("increase2")
        elif(p>l[i] and a[p]<a[p-1] and pq==r[i]):
          increase=increase +1
          print("increase3")
        elif( pq<r[i] and a[pq]>a[pq+1] and p==l[i]):
          increase=increase+1
          print("increase4")
    
      flag=0
  
      flag=all(i > j for i, j in zip(alpha, alpha[1:]))
      if(flag):
        # print("decrease")
        if(p==l[i] and pq==r[i]):
          decrease=decrease+1
          print("decrease")
        elif( (p>l[i] and a[p]>a[p-1]) and (pq<r[i] and a[pq]<a[pq+1])):
         decrease=decrease +1
         print("decrease2")
        elif( p>l[i] and a[p]>a[p-1] and pq==r[i]):
         decrease=decrease +1
         print("decrease3")
        elif( pq<r[i] and a[pq]<a[pq+1] and p==l[i]):
          decrease=decrease+1
          print("decrease4")

  if(increase==decrease):
    print("YES")
  else:
    print("NO")
      




    # print(bin)

# a=[0,0,1,0]
# print(a.index(1))
# print(a[::-1].index(1))




# bin=[]
# for i in range(2**4):
#   print(binary(i,4))
# # print(bin)
# alpha=[3,2,1,0]
# flag = all(i > j for i, j in zip(alpha, alpha[1:]))
# print(flag)
