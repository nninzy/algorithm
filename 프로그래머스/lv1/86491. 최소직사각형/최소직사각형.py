def solution(sizes):
    sizes = list(map(sorted, sizes))
    width = max(item[0] for item in sizes)
    height = max(item[1] for item in sizes)
    answer = width * height
    return answer