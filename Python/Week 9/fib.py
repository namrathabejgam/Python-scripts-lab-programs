n=int(input())
c=0
a=0
b=1
while(c<=n):
  print(c,end=' ')
  a=b
  b=c
  c=a+b
