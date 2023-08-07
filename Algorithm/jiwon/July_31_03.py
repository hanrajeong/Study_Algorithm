#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/70129
#   분류 : [월간 코드 챌린지 시즌2] 이진 변환 반복하기

def solution(x):
    answer = []
    
    cnt = 0
    zero = 0
    
    while True:
        if x == '1':
            break
        zero = zero + x.count("0")
        x = x.replace("0", "")
        
        x = bin(len(x))[2:]
        
        cnt = cnt + 1
    
    answer = [cnt, zero]
    
    return answer