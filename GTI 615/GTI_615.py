x=list(map(int,input().split()))
y=int(input())
z=[]
for a in range(x[0]):
  f=list(map(str,input().split()))
  z.append(f)
k=[]
p=int(input())
for a in range(y-1,x[1]-y+1):
  k.append(z[y-1][a])

for a in range(y,x[0]-y+1):
  k.append(z[a][x[1]-y])
if y-1 !=x[0]-y:
  for a in range(x[1]-y-1,y-2,-1):
    k.append(z[x[0]-y][a])
if y-1 != x[1]-y:
  for a in range(x[0]-y-1,y-1,-1):
    k.append(z[a][y-1])

for a in k:
  if chr(ord(a)+p).isalpha():
    print(chr(ord(a)+p),end="")
