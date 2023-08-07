# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    ret = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1 = s2 = s3 = 0
    for idx, answer in enumerate(answers):
        if answer == p1[idx%len(p1)]:
            s1 += 1
        if answer == p2[idx%len(p2)]:
            s2 += 1
        if answer == p3[idx%len(p3)]:
            s3 += 1
    maxS = max(s1, s2, s3)
    score = [s1, s2, s3]
    for idx, s in enumerate(score):
        if s == maxS:
            ret.append(idx + 1)
    return ret