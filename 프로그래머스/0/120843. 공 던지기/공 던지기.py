def solution(numbers, k):
    position = ((k-1) * 2) % len(numbers)
    return numbers[position]