A, B, V = map(int, input().split())
day_n =  (V - B) // (A - B)
if (V - B) % (A - B) > 0:
    day_n += 1
print(day_n)