def solution(quiz):
    answer = []
    for q in quiz:
        parts = q.split()
        x = int(parts[0])
        op = parts[1]
        y = int(parts[2])
        z = int(parts[4])
        
        if op == '+':
            if x + y == z:
                answer.append("O")
            else:
                answer.append("X")
        elif op == '-':
            if x - y == z:
                answer.append("O")
            else:
                answer.append("X")
    return answer