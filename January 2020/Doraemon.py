t = input()
for i in range(int(t)):
  n=list(map(int,input().split()))
  matrix=[]
  for i in range(n[0]):
    matrix.append(list(map(int,input().split())))
  count=0
  for c in range(min(n[0],n[1])//2+1):
    # print(c)
    # if c%2!=0:
    for i in range(c,n[0]-c ):
      for j in range(c,n[1]-c):
        # print(i,j)
        arr1 = [matrix[k][j] for k in range(i-c,i+c+1)]
        arr2 = matrix[i][j-c:j+c+1]
        # print(arr1," ",arr2)
        if((arr1==arr1[::-1]) and (arr2==arr2[::-1])):
          count=count+1
        
  print(count)