x=input().strip()
y=input().strip()
t=0
f,g=[],[]
for a in range(len(x)//5):
  f.append(x[t:t+5][::-1])
  t+=5
if len(x)>t-5:
  f.append(x[t:][::-1])
t=0
for b in range(len(y)//5):
  g.append(y[t:t+5][::-1])
  t+=5
if len(y)>t-5:
  g.append(y[t:][::-1])
f=f+g
f=''.join(f)
k=[]
t,s='',-1
for a in range(len(f)):
  if f[a].isalpha() or f[a].isdigit():
    k.append([f[a],0])
    t=f[a]
    s+=1
  else:
    
    k[s][1]+=1

k=sorted(k,key=lambda x:x[1])
for a in k:
  print(a[0],end="")
