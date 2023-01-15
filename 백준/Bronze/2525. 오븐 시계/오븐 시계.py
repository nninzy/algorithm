A,B = map(int,input().split())
cooking = int(input())
total = (A * 60) + B + cooking
total = total - (24*60) if total >= (24*60) else total
print(*divmod(total, 60))