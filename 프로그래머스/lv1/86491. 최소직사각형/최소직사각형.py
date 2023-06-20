def solution(sizes):
    width = []
    height = []
    
    for item in sizes:
        width.append(max(item))
        height.append(min(item))
    answer = max(width) * max(height)
    return answer