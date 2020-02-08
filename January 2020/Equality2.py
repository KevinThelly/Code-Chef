# cook your dish here


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

# increase=0
# decrease=0
alpha=[]
p=[]
pq=[]
for i in range(n[0]-1):
  for j in range(i+1,n[0]):
    alpha.append(a[i:j+1])
    p.append(i)
    pq.append(j)
    # print(a[i:j+1],p,pq)
# print(alpha,p,pq)

for i in range(len(val)):
  # print(val[i])
  increase=0
  decrease=0
  for k in range(len(alpha)):
    # print(alpha[k],p[k],pq[k])
    temp=alpha[k]
    flag=0
    flag = all(i < j for i, j in zip(temp, temp[1:]))
    if(flag):
      # print("increase",alpha[k])
      if(p[k]==l[i] and pq[k]==r[i]):
        # print("increase1")
        increase=increase+1
      elif( (p[k]>l[i] and a[p[k]]<a[p[k]-1]) and (pq[k]<r[i] and a[pq[k]]>a[pq[k]+1])):
        increase=increase +1
        # print("increase2")
      elif(p[k]>l[i] and a[p[k]]<a[p[k]-1] and pq[k]==r[i]):
        increase=increase +1
        # print("increase3")
      elif( pq[k]<r[i] and a[pq[k]]>a[pq[k]+1] and p[k]==l[i]):
        increase=increase+1
        # print("increase4")
      continue


    flag=0
    flag = all(i > j for i, j in zip(temp, temp[1:]))
    if(flag):
      # print("increase",alpha[k])
      if(p[k]==l[i] and pq[k]==r[i]):
        # print("deccrease1")
        decrease=decrease+1
      elif( (p[k]>l[i] and a[p[k]]>a[p[k]-1]) and (pq[k]<r[i] and a[pq[k]]<a[pq[k]+1])):
        decrease=decrease+1
        # print("deccrease2")
      elif(p[k]>l[i] and a[p[k]]>a[p[k]-1] and pq[k]==r[i]):
        decrease=decrease+1
        # print("deccrease3")
      elif( pq[k]<r[i] and a[pq[k]]<a[pq[k]+1] and p[k]==l[i]):
        decrease=decrease+1
        # print("decrease4")
  # print("increase",increase)
  # print("decrease",decrease)
  if(increase==decrease):
    print("YES")
  else:
    print("NO")

# a=[1,2,3]
# for i in range(3):
#   print(a[1:3])