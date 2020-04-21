T=int(input())
mod=998244353

for t in range(T):
  L=input()
  vand={ "0": 9, "1": 1, "a": 3, "A": 3  }
  vor={ "0": 1, "1": 9, "a": 3, "A": 3  }
  vxor={ "0": 4, "1": 4, "a": 4, "A": 4  }
  v={ "0": 1, "1": 1, "a": 1, "A": 1 }

  
  hashcount=L.count("#")

  if(hashcount==1):
    product=pow(4,mod-2,mod)
    print(product,product,product,product)
    continue    

  if(L[0]!="("):
    L="(" + L +")"

  a=[]
  for i in range(len(L)):
    if(L[i]=="("):
      a.append("(")
    elif(L[i]==")"):
      if(L[i-4]=="("):
        if(L[i-2]=="&"):
          a.pop()
          a.append(vand)
        if(L[i-2]=="|"):
          a.pop()
          a.append(vor)
        if(L[i-2]=="^"):
          a.pop()
          a.append(vxor)
      else:
        a.append(")")
    if(L[i]=="&" or L[i]=="|" or L[i]=="^" ):
      if(L[i-1]==")" and L[i+1]=="("):
        a.append(L[i])
      elif(L[i-1]=="#" and L[i+1]=="("):
        a.append(v)
        a.append(L[i])
      elif(L[i-1]==")" and L[i+1]=="#"):
        a.append(L[i])
        a.append(v)
  print(a)
  
  
  while(")" in a):
    i=a.index(")")
    print(a[i-3],a[i-1])
    # while(i!="("):
    t0,t1,ta,tA=1,1,1,1
    if(a[i-2]=="&"):
      t0=a[i-3]["0"]*(a[i-1]["0"] + a[i-1]["1"] + a[i-1]["a"] + a[i-1]["A"])   + a[i-3]["a"]*(a[i-1]["0"] + a[i-1]["A"]) + a[i-3]["A"]*(a[i-1]["0"] + a[i-1]["a"]) + a[i-3]["1"]*(a[i-1]["0"]) 

      t1=a[i-3]["1"]*a[i-1]["1"]
      ta=a[i-3]["1"]*a[i-1]["a"] + a[i-3]["a"]*(a[i-1]["1"] + a[i-1]["a"])
      tA=a[i-3]["1"]*a[i-1]["A"] + a[i-3]["A"]*(a[i-1]["1"] + a[i-1]["A"])
    
    if(a[i-2]=="|"):
      t1=a[i-3]["1"]*(a[i-1]["0"] + a[i-1]["1"] + a[i-1]["a"] + a[i-1]["A"])   + a[i-3]["a"]*(a[i-1]["1"] + a[i-1]["A"]) + a[i-3]["A"]*(a[i-1]["1"] + a[i-1]["a"]) + a[i-3]["0"]*(a[i-1]["1"]) 

      t1=a[i-3]["1"]*a[i-1]["1"]
      ta=a[i-3]["1"]*a[i-1]["a"] + a[i-3]["a"]*(a[i-1]["1"] + a[i-1]["a"])
      tA=a[i-3]["1"]*a[i-1]["A"] + a[i-3]["A"]*(a[i-1]["1"] + a[i-1]["A"])
    
    if(a[i-2]=="^"):
      t0=a[i-3]["1"]*a[i-1]["0"] + a[i-3]["0"]*a[i-1]["1"] + a[i-3]["a"]*a[i-1]["A"] + a[i-3]["A"]*a[i-1]["a"]

      t1=a[i-3]["1"]*a[i-1]["1"] + a[i-3]["0"]*a[i-1]["0"] + a[i-3]["a"]*a[i-1]["a"] + a[i-3]["A"]*a[i-1]["A"]

      ta=a[i-3]["1"]*a[i-1]["A"] + a[i-3]["A"]*a[i-1]["1"] + a[i-3]["0"]*a[i-1]["a"] + a[i-3]["a"]*a[i-1]["0"]

      tA=a[i-3]["1"]*a[i-1]["a"] + a[i-3]["a"]*a[i-1]["1"] + a[i-3]["0"]*a[i-1]["A"] + a[i-3]["A"]*a[i-1]["0"]
      
    a[i-3]["0"],a[i-3]["1"],a[i-3]["a"],a[i-3]["A"]=t0,t1,ta,tA
    a.pop(i-1)
    i=a.index(")")
    a.pop(i-1)
    i=a.index(")")
    a.pop(i-2)
    i=a.index(")")
    a.pop(i)
    print(a)
  
  d=int(pow(4,hashcount))
  product=pow(d,mod-2,mod)

  print((a[0]["0"]*product)%mod,(a[0]["1"]*product)%mod,(a[0]["a"]*product)%mod,(a[0]["A"]*product)%mod)
  
        