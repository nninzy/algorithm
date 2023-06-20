def solution(sizes):
    width = 0
    height = 0
    
    for item in sizes:
        width = max(max(item), width)
        height = max(min(item), height)
    answer = width * height
    return answer