
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

rate_board = [[0, 0, 2, 0, 0],
              [0, 10, 7, 1, 0],
              [5, 0, 0, 0, 0],
              [0, 10, 7, 1, 0],
              [0, 0, 2, 0, 0]]
ret = 0


def rotate(_arr):
    return list(map(list, zip(*_arr)))[::-1]


def move_sand(_board, _rate, y, x, d, n):
    global ret

    cur_sand, ny, nx = _board[y][x], y + dy[d], x + dx[d]
    for i in range(5):
        for j in range(5):
            if _rate[i][j] > 0:
                by, bx = y + i - 2, x + j - 2
                move = _board[y][x] * _rate[i][j] // 100
                if -1 < bx < n and -1 < by < n:
                    _board[by][bx] += move
                else:
                    ret += move
                cur_sand -= move
    if -1 < ny < n and -1 < nx < n:
        _board[ny][nx] += cur_sand
    else:
        ret += cur_sand
    _board[y][x] = 0


def solution(_board, n):
    global rate_board
    y, x, d, can = n // 2, n // 2, 0, 1
    final = 2
    rate_boards = [rate_board]
    for i in range(3):
        rate_board = rotate(rate_board)
        rate_boards.append(rate_board)

    while not (y == 0 and x == -1):
        for i in range(final):
            for j in range(can):
                y, x = y + dy[d], x + dx[d]
                rate = rate_boards[d]
                move_sand(_board, rate, y, x, d, n)
            d = (d + 1) % 4
        can += 1
        if can == n:
            final = 1
    print(ret)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    solution(board, n)