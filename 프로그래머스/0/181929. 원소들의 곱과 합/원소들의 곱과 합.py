import math
def solution(num_list):
    a = math.prod(num_list)
    b = sum(num_list)**2
    if a<b:
        return 1
    else : 
        return 0