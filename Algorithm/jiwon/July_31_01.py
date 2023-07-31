#   백준 문제 풀이
#   https://www.acmicpc.net/problem/2563
#   분류 : [구현] 2563번 색종이

arr = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  for row in range(x, x+10):
    for col in range(y, y+10):
      arr[row][col] = 1

result = 0

for j in arr:
  result+=j.count(1)
  
print(result)
  