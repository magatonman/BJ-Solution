#input

n=int(input())
numbers=list(map(int, input().split()))
x=int(input())

numbers.sort()

#generate pointers and result
a=0
b=n-1
ret=0

#calculation
while a<b:
  add=numbers[a]+numbers[b]
  if add==x:
    ret+=1
    a+=1
  elif add>x:
    b-=1
  elif add<x:
    a+=1

print(ret)
