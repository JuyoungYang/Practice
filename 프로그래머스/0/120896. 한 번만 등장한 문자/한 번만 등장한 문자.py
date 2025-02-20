def solution(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    unique_chars = []
    for char in char_counts:
        if char_counts[char] == 1:
            unique_chars.append(char)

    unique_chars.sort()
    return "".join(unique_chars)