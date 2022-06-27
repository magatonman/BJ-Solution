import heapq

#input
n, m=map(int, input().split())
cards=list(map(int, input().split()))

heap=[]

#put inputs to min heap
for i in cards:
  heapq.heappush(heap, i)

#solve
for i in range(m):
  x=heapq.heappop(heap)
  y=heapq.heappop(heap)
  for j in range(2):
    heapq.heappush(heap, x+y)

print(sum(heap))
