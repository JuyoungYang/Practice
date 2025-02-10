def solution(order):
    count = sum(1 for digit in str(order) if digit in "369")
    return count
