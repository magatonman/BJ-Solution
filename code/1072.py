X, Y=map(int, input().split())

def winrate(i):
  return (Y+i)*100//(X+i)

default=winrate(0)

if winrate(X)==default:
  print(-1)
else:
  #binary search
  ret=0
  p=0
  q=X
  while p<=q:
    mid=(p+q)//2
    if default<winrate(mid):
      ret=mid
      q=mid-1
    else:
      p=mid+1
  print(ret)
