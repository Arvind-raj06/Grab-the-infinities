
x=input().strip()
y=''
for a in x:
  y+=chr(ord(a)-9)
print(y[-3:]+y[:-3])
