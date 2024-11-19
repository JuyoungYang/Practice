def solution(ineq, eq, n, m):
    if ineq == ">":  
        if eq == "=":  
            return 1 if n >= m else 0
        elif eq == "!":  
            return 1 if n > m else 0
    elif ineq == "<":  
        if eq == "=":  
            return 1 if n <= m else 0
        elif eq == "!":  
            return 1 if n < m else 0