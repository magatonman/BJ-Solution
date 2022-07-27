N=int(input())
memoization=[0, 0, 1, 1]
for i in range(4, N+1):
  memoization.append(memoization[-1]+1)
  if i%2==0:
    memoization[i]=min(memoization[i], memoization[i//2]+1)
  if i%3==0:
    memoization[i]=min(memoization[i], memoization[i//3]+1)

print(memoization[N])
