def solution(keyinput, board):
    x, y = 0, 0
    x_limit = board[0] // 2
    y_limit = board[1] // 2

    for key in keyinput:
        if key == "up":
            if y + 1 <= y_limit:
                y += 1
        elif key == "down":
            if y - 1 >= -y_limit:
                y -= 1
        elif key == "left":
            if x - 1 >= -x_limit:
                x -= 1
        elif key == "right":
            if x + 1 <= x_limit:
                x += 1
    return [x, y]