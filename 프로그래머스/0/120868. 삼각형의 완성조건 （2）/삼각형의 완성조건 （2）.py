def solution(sides):
    side1 = sides[0]
    side2 = sides[1]

    min_side = min(side1, side2)
    answer = 2 * min_side - 1

    return answer