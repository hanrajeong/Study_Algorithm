#구현
#https://www.acmicpc.net/problem/5635
n = int(input())
arr = []

for _ in range(n):
  a, b, c, d = list(map(str, input().split()))
  temp = [a,int(b),int(c),int(d)]
  arr.append(temp)

#오름차순 정렬
arr.sort(key=lambda a: (a[3], a[2], a[1]))

#맨앞= 나이많은사람, 맨뒤=나이적은사람
print(arr[-1][0])
print(arr[0][0])

#https://www.acmicpc.net/problem/1343
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)

