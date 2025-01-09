def count_repaint(board, start_row, start_col, start_with_white):
    count = 0
    for i in range(8):
        for j in range(8):
            current = board[start_row + i][start_col + j]

            if start_with_white:
                should_be_white = (i + j) % 2 == 0
            else:
                should_be_white = (i + j) % 2 == 1
                
            if (should_be_white and current == 'B') or (not should_be_white and current == 'W'):
                count += 1
    
    return count

N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_count = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        white_start = count_repaint(board, i, j, True)
        black_start = count_repaint(board, i, j, False)
        min_count = min(min_count, white_start, black_start)

print(min_count)