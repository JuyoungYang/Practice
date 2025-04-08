def solution(spell, dic):
    spell_sorted = sorted(spell)
    
    for word in dic:
        if sorted(word) == spell_sorted:
            return 1
    return 2
