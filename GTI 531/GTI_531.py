x=int(input())
z=[]
for a in range(x):
  y=list(map(str,input().split()))
  z.append(y)
p=list(map(str,input().split(',')))
for a in z:
  if p[0][1]=='+':
    a[1]=int(a[1])+int(p[0][2:])
  elif p[0][1]=='-':
    a[1]=int(a[1])-int(p[0][2:])
  elif p[0][1]=='/':
    a[1]=int(a[1])/int(p[0][2:])
  else:
    a[1]=int(a[1])*int(p[0][2:])
    
z=sorted(z, key=lambda x:x[1])
for a in range(int(p[1])):
  print(z[a][0],end="")
