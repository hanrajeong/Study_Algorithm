#https://www.acmicpc.net/problem/1337

n = int(input())
arr = []

for _ in range(n):
  arr.append(int(input()))

arr.sort()

temp = []
for i in range(n):
  cnt = 0
  for j in range(arr[i], arr[i]+5):
    if j not in arr:
      cnt +=1
  temp.append(cnt)

print(min(temp))



