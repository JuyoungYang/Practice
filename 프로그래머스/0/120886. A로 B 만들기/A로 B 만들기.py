def solution(before, after):
    before_sorted = sorted(before)
    after_sorted = sorted(after)
    
    if before_sorted == after_sorted:
        return 1
    else:
        return 0