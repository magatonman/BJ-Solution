division=1000000009
#create and set a default value of memoization
memoization=[0 for i in range(1000001)]

memoization[1]=1
memoization[2]=2
memoization[3]=4

#solving
def solve(n):
  if memoization[n]!=0:
    return memoization[n]
  else:
    for i in range(4, n+1):
      if memoization[i]!=0:
        continue
      memoization[i]=(memoization[i-1]+memoization[i-2]+memoization[i-3])%division
    return memoization[n]

#input and using solve function
T=int(input())
for i in range(T):
  n=int(input())
  print(solve(n))
