N=int(input())
left=list(map(int, input().split()))
right=list(map(int, input().split()))
memoization=[[-1 for i in range(N+1)] for j in range(N+1)]
def solve(l, r):
  if l==N or r==N:
    return 0
  if memoization[l][r]!=-1:
    return memoization[l][r]
  memoization[l][r]=0
  if left[l]>right[r]:
    memoization[l][r]+=(solve(l, r+1)+right[r])
  else:
    memoization[l][r]=max(solve(l+1, r+1), solve(l+1, r))
  return memoization[l][r]

print(solve(0, 0))
