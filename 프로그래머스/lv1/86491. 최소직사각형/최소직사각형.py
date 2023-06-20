def solution(sizes):
    width = []
    height = []
    
    for item in sizes:
        if item[0] > item[1]:
            width.append(item[0])
            height.append(item[1])
        else:
            width.append(item[1])
            height.append(item[0])
    answer = max(width) * max(height)
    return answer