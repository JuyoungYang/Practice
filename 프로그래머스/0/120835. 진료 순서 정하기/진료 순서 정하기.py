def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    
    rank_dict = {}

    for rank, value in enumerate(sorted_emergency, 1):
        rank_dict[value] = rank
    
    return [rank_dict[value] for value in emergency]