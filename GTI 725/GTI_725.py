x=input().strip()
y=input().strip()
a=input().strip()[::-1]
b=input().strip()[::-1]
f=min(len(a),len(b),len(x),len(y))
minlen = min(len(a),len(b))
ninlen = min(len(x),len(y))
res = "".join(["".join(x+y for x,y in zip(x,y)),x[ninlen:],y[ninlen:]])
res1 = "".join(["".join(x+y for x,y in zip(a,b)),a[minlen:],b[minlen:]])
res=res+res1

print(res[-f:]+res[:len(res)-f])
