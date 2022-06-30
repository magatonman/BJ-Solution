# create memoization array
memoization=[[[1 for i in range(21)] for j in range(21)] for k in range(21)]

memoization[20][20][20]=1048576

# solve
def solve(a, b, c):
  # base statements
  if a<=0 or b<=0 or c<=0:
    return 1
  elif a>20 or b>20 or c>20:
    return memoization[20][20][20]
  # if a algorithm previous calculated answer, return it;
  elif memoization[a][b][c]!=1:
    return memoization[a][b][c]
  elif a<b and b<c:
    ret=solve(a, b, c-1)+solve(a, b-1, c-1)-solve(a, b-1, c)
    memoization[a][b][c]=ret
    return ret
  else:
    ret=solve(a-1, b, c)+solve(a-1, b-1, c)+solve(a-1, b, c-1)-solve(a-1, b-1, c-1)
    memoization[a][b][c]=ret
    return ret

while True:
  a, b, c=map(int, input().split())
  if (a, b, c)==(-1, -1, -1):
    break
  else:
    print("w("+str(a)+", "+str(b)+", "+str(c)+") = "+str(solve(a, b, c)))
