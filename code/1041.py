N=int(input())
A, B, C, D, E, F=map(int, input().split())

#calculate all possible cases for upper corners: ABC, ABD, ACE, ADE, FBC, FBD, FCE, FDE

three_eyes=min(A+B+C, A+B+D, A+C+E, A+D+E, F+B+C, F+B+D, F+C+E, F+D+E)

#calculate all possible cases for lower corners and upper & middle sides excpet corners: AB, AC, AD, AE, BC, BD, BF, CE, CF, DE, DF

two_eyes=min(A+B, A+C, A+D, A+E, B+C, B+D, B+F, C+E, C+F, D+E, D+F, E+F)

len_without_corners=N-2

#solve corner case: N is 1
if N==1:
  print(A+B+C+D+E+F-max(A, B, C, D, E, F))
#solving other cases
else:
  ret=0
  ret+=three_eyes*4
  ret+=two_eyes*4
  #calculate when N>2
  if len_without_corners>0:
    ret+=two_eyes*len_without_corners*8
    ret+=min(A, B, C, D, E, F)*((len_without_corners+1)*len_without_corners*4+len_without_corners**2)
  print(ret)
