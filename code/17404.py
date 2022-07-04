N=int(input())
house=[]
for i in range(N):
  rgb=list(map(int, input().split()))
  house.append(rgb)

ret=1000000007

for i in range(3):
  memoization=[[1000000007, 1000000007, 1000000007] for i in range(N)]
  memoization[0][i]=house[0][i]
  for j in range(1, N):
    memoization[j][0]=min(memoization[j-1][1], memoization[j-1][2])+house[j][0]
    memoization[j][1]=min(memoization[j-1][2], memoization[j-1][0])+house[j][1]
    memoization[j][2]=min(memoization[j-1][0], memoization[j-1][1])+house[j][2]
  for j in range(3):
    if i!=j:
      ret=min(ret, memoization[-1][j])

print(ret)
