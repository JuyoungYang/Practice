from math import gcd
def solution(numer1, denom1, numer2, denom2):
    #분모 denom1*denom2 
    #분자 (numer1*denom2)+(numer2*denom1)
    a = (denom1 * denom2) // gcd(denom1, denom2)
    new_numer = numer1 * (a // denom1) + numer2 * (a // denom2)
    new_denom = a
    b = gcd(new_numer, new_denom)
    last_numer = new_numer // b
    last_denom = new_denom // b
    answer = [last_numer, last_denom]
    return answer