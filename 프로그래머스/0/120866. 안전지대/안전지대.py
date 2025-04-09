def solution(board):
    n = len(board)
    if n == 0:
        return 0

    danger_zone = [[0 for _ in range(n)] for _ in range(n)]

    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),  (0, 0),  (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for dr, dc in offsets:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        danger_zone[nr][nc] = 1

    safe_count = 0
    for r in range(n):
        for c in range(n):
            if danger_zone[r][c] == 0:
                safe_count += 1

    return safe_count