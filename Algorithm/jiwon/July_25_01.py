#   백준 문제 풀이
#   https://www.acmicpc.net/problem/2303
#   분류 : [구현] 2303번 숫자 게임
from itertools import combinations
N = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(N)]
answer = 0
answer_max = 0
for i in range(N):
    comb = list(combinations(arr[i], 3))
    temp = 0
    for j in comb:
        temp = max(temp, sum(j)%10)
    if temp >= answer_max:
        answer = i+1
        answer_max = temp

print(answer)


