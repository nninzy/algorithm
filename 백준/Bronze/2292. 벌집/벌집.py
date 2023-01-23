N = int(input())
step = 1; step_total = 1
while step_total < N :
    step_total += 6 * step
    step += 1
print(step)