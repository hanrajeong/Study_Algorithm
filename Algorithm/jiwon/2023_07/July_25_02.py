#   백준 문제 풀이
#   https://www.acmicpc.net/problem/16922
#   분류 : [구현] 16922번 로마 숫자 만들기
from itertools import combinations_with_replacement
n = int(input())
result = []
numbers = [1, 5, 10, 50]

for temp in combinations_with_replacement(range(4), n):
    #temp  = (1,2)   (1,3)   (1,4)
    sum = 0
    for i in temp:
        sum += numbers[i]
    result.append(sum)

print(len(set(result)))
