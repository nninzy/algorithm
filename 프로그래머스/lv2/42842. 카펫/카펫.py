def solution(brown, yellow):
    answer = []
    y_primes = []       
    for num in range(1, yellow+1):
        if yellow%num == 0:
            num2 = yellow//num
            cal = 2 * (num + num2 + 2)
            if brown == cal:
                answer = [num2 + 2] + [num + 2]
                break
    return answer