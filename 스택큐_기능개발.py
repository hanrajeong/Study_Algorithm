def solution(progresses, speeds):
    answer = []
    time = 0 #진도일 
    count = 0 #answer에 담길 값
    
    while len(progresses) > 0:
        if progresses[0] + time*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1

        #진도율이 총 100이 안넘으면,
        else:   
            #그리고, count가 0보다 클 때,
            if count > 0:
                answer.append(count)
                #count 초기화
                count = 0  
            #time은 1씩 증가한다. 
            time+=1
    answer.append(count)
    return answer