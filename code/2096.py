N=int(input())

# saving temporal results
memoization_max=[0, 0, 0]
memoization_min=[0, 0, 0]

for i in range(N):
  # input
  a, b, c=map(int, input().split())

  # make a variable which means particular position of result array
  first_max=memoization_max[0]
  second_max=memoization_max[1]
  third_max=memoization_max[2]
  
  first_min=memoization_min[0]
  second_min=memoization_min[1]
  third_min=memoization_min[2]

  # calculating result's answer
  a2_max=max(first_max, second_max)+a
  b2_max=max(first_max, second_max, third_max)+b
  c2_max=max(second_max, third_max)+c
  # renew an array
  memoization_max=[a2_max, b2_max, c2_max]

  # do a same way to solve minimum problem
  a2_min=min(first_min, second_min)+a
  b2_min=min(first_min, second_min, third_min)+b
  c2_min=min(second_min, third_min)+c
  memoization_min=[a2_min, b2_min, c2_min]

print(max(memoization_max), min(memoization_min))
