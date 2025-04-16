def solution(lines):
    line_count = [0] * 201
    
    for start, end in lines:
        for i in range(start + 100, end + 100):
            line_count[i] += 1    
    return len([count for count in line_count if count >= 2])