#   백준 문제 풀이
#   https://www.acmicpc.net/problem/11637
#   분류 : [구현] 인기 투표

t = int(input())

for _ in range(t):
  n = int(input())
  arr = []
  for _ in range(n):
    arr.append(int(input()))
  
  max_index = arr.index(max(arr)) +1
  if arr.count(max(arr)) >1:
    print("no winner")
  else:
    if sum(arr)-max(arr)<max(arr):
      print('majority winner',max_index)
    else:
      print('minority winner',max_index)
    

