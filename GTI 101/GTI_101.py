def spiral(m, n, a):
  k = 0
  l = 0
  f=[]
  while (k < m and l < n):
    for i in range(l, n):
      f.append(a[k][i])
    k += 1
    
    for i in range(k, m):
      f.append(a[i][n - 1])
    n -= 1
 
    if (k < m):
      for i in range(n - 1, (l - 1), -1):
        f.append(a[m - 1][i])
      m -= 1
    
    if (l < n):
      for i in range(m - 1, k - 1, -1):
        f.append(a[i][l])
      l += 1
      
  return f
x=list(map(int,input().split()))
z=[]
for a in range(x[0]):
  y=list(map(int,input().split()))
  z.append(y)
t=spiral(x[0],x[1],z)
for a in t:
  print(chr(int(str(a),8)),end="")
