#   백준 문제 풀이
#   https://www.acmicpc.net/problem/2161
#   분류 : [구현] 2161번 카드1

n = int(input())
card = [i for i in range(1, n + 1)]
discard = []
while len(card) != 1:
    discard.append(card.pop(0))
    card.append(card.pop(0))   
for c in discard:
    print(c, end=' ')
print(card[0])
