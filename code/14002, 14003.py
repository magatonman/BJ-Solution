import bisect # 이진 탐색 모듈
N=int(input())
A=list(map(int, input().split()))
memoization=[1 for i in range(N)]
compare=[A[0]]

for i in range(N):
  if A[i]>compare[-1]:
    compare.append(A[i])
    memoization[i]=len(compare)-1
  else:
    memoization[i]=bisect.bisect_left(compare, A[i])
    compare[memoization[i]]=A[i]

maximum=max(memoization)+1
ret=[]
for i in range(N-1, -1, -1):
  if memoization[i]==maximum-1:
    ret.append(A[i])
    maximum=memoization[i]
print(len(ret))
print(*ret[::-1])
