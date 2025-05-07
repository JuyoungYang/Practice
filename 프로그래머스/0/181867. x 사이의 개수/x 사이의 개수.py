def solution(myString):
    parts = myString.split('x')
    return [len(part) for part in parts]
