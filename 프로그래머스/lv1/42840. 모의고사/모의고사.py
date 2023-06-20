def equal(asr,my_asr):
    answer = 0
    for i in range(len(asr)):
        if asr[i] == my_asr[i%len(my_asr)]:
            answer += 1
    return answer

def solution(answers):
    answer = []
    supo = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    corrects = list(equal(answers, supoza) for supoza in supo)
    max_cnt = max(corrects)
    for i in range(3):
        if corrects[i] == max_cnt:
            answer.append(i+1)
    return answer