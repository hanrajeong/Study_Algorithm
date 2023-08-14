#구현 풀이 3문제
#https://www.acmicpc.net/problem/11536
n= int(input())

arr =[]

for _ in range(n):
  arr.append(input())

if sorted(arr) == arr:
  print('INCREASING')
elif sorted(arr, reverse=True) == arr:
  print('DECREASING')
else:
  print('NEITHER')

#https://www.acmicpc.net/problem/11576
n = int(input())
arr = []
answer = 0
task = []
for _ in range(n):
  arr.append(list(map(int, input().split())))


for i in range(n):
  if arr[i][0] == 1:
    task.append((arr[i][1], arr[i][2]))
    
  if task:
    score, time = task.pop()
    time -=1
    if time == 0:
      answer += score
    else:
      task.append((score, time))

print(answer)

#https://www.acmicpc.net/problem/1235
n=int(input())
nums=[]
for _ in range(n):
    nums.append(str(input()))
for i in range(1, len(nums[0])+1):
    results=[]
    for j in range(n):
        if nums[j][-i:] in results:
            break
        else:
            results.append(nums[j][-i:])
    if len(results)==n:
        print(i)
        break