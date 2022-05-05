import collections

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

dd = {(0, 1): 0, (-1, 0): 1, (0, -1): 2, (1, 0): 3}

def change_dice(_dice, d):
    tmp = _dice[6]
    if d == 0:
        _dice[6], _dice[3], _dice[1], _dice[4] = _dice[3], _dice[1], _dice[4], tmp

    if d == 1:
        _dice[6], _dice[2], _dice[1], _dice[5] = _dice[2], _dice[1], _dice[5], tmp

    if d == 2:
        _dice[6], _dice[4], _dice[1], _dice[3] = _dice[4], _dice[1], _dice[3], tmp

    if d == 3:
        _dice[6], _dice[5], _dice[1], _dice[2] = _dice[5], _dice[1], _dice[2], tmp


def count_c(_board, _n, _m, _y, _x):
    cur = _board[_y][_x]
    que = collections.deque()
    que.append([_y, _x])
    visit = [[0] * _m for _ in range(_n)]
    visit[_y][_x] = 1
    c = 1
    while len(que) != 0:
        cy, cx = map(int, que.popleft())
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if -1 < ny < _n and -1 < nx < _m and visit[ny][nx] == 0 and _board[ny][nx] == cur:
                que.append([ny, nx])
                c += 1
                visit[ny][nx] = 1
    return c


def solution(_board, _n, _m, _k):
    d, dice = 0, [0, 1, 2, 3, 4, 5, 6]
    y, x, ret = 0, 0, 0
    for i in range(_k):
        if -1 < y + dy[d] < _n and -1 < x + dx[d] < _m:
            y, x = y + dy[d], x + dx[d]
        else:
            d = dd[(-dy[d], -dx[d])]
            y, x = y + dy[d], x + dx[d]
        change_dice(dice, d)
        if dice[6] > _board[y][x]:
            d = (d - 1) % 4
        elif dice[6] < _board[y][x]:
            d = (d + 1) % 4
        score = _board[y][x] * count_c(_board, _n, _m, y, x)
        ret += score

    print(ret)


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
solution(board, n, m, k)