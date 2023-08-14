#   백준 문제 풀이
#   https://www.acmicpc.net/problem/2669
#   분류 : [구현] 2669 직사각형 네개의 합집합의 면적 구하기 

arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x1, x2):
    for j in range(y1, y2):
      arr[i][j] =1


answer = 0

for i in arr:
  answer += sum(i)
print(answer)
