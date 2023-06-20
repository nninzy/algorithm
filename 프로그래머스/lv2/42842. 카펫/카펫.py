def solution(brown, yellow):
    answer = []
    y_primes = []
    for i in range(1, yellow+1):
        if yellow%i == 0:
            y_primes.append(i)
    for num in y_primes:
        num2 = yellow//num
        calculate = 2 * (num + num2 + 2)
        if brown == calculate:
            answer = [num2 + 2] + [num + 2]
            break
    return answer