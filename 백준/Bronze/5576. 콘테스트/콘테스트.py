k = []; w = [];
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
print(sum(sorted(w)[7:]), sum(sorted(k)[7:]))