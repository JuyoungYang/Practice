def solution(score):
    # 평균 점수 계산
    avg_scores = [(s[0] + s[1]) / 2 for s in score]

    # 평균 점수 인덱스
    indexed_scores = list(enumerate(avg_scores))

    # 평균 점수 내림차순 정렬
    sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)

    # 등수 계산
    ranks = [0] * len(score)
    current_rank = 1
    for i, (idx, avg) in enumerate(sorted_scores):
        if i > 0 and avg == sorted_scores[i - 1][1]:
            ranks[idx] = ranks[sorted_scores[i - 1][0]]
        else:
            ranks[idx] = current_rank
        current_rank += 1

    return ranks
