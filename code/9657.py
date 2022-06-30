N=int(input())
memoization=[0 for i in range(1005)]
memoization[1]=1
memoization[2]=0
memoization[3]=1
memoization[4]=1
if N>=5:
  for i in range(5, N+1):
    memoization[i]=max(memoization[i], not(memoization[i-1]))
    memoization[i]=max(memoization[i], not(memoization[i-3]))
    memoization[i]=max(memoization[i], not(memoization[i-4]))

print("SK" if memoization[N]==1 else "CY")
