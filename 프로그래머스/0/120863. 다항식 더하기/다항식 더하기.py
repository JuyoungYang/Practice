def solution(polynomial):
    x_coef = 0
    const = 0
    
    terms = polynomial.split(" + ")
    
    for term in terms:
        if "x" in term:
            if term == "x":
                x_coef += 1
            else:
                x_coef += int(term[:-1])
        else:
            const += int(term)
            
    result = ""
    
    if x_coef > 0:
        if x_coef == 1:
            result += "x"
        else:
            result += str(x_coef) + "x"
    
    if const > 0:
        if result != "":
            result += " + " + str(const)
        else:
            result += str(const)
            
    return result