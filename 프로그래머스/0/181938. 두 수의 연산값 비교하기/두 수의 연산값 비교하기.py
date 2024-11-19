def solution(a, b):
    ab = int(str(a) + str(b)) 
    product = 2 * a * b  
    return ab if ab >= product else product
