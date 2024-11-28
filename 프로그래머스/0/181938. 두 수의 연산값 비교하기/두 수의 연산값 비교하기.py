def solution(a, b):
    ab = int(str(a) + str(b))
    return ab if ab >= 2 * a * b else 2 * a * b
