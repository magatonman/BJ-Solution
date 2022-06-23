N=int(input())

#A dictionary for input data
councel={}

#An array for results of each time
memoization=[0 for i in range(N+1)]

#input
for i in range(1, N+1):
  T, P=map(int, input().split())

  #if an input councel is unable, then discard
  if i-1+T<=N:
    councel[i]=[T, P]

#solve
for i in councel:
  T=councel[i][0]
  P=councel[i][1]
  #finding maximum value of income before ith day's counceling
  #then, compare the value with previous maximum value of i+T-1th day
  memoization[i+T-1]=max(memoization[i+T-1], max(memoization[0:i])+P)

print(max(memoization))
