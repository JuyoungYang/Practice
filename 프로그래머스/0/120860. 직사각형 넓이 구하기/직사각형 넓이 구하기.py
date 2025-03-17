def solution(dots):
    x = []
    y = []
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    
    width = max(x) - min(x)
    height = max(y) - min(y)
    
    return width * height