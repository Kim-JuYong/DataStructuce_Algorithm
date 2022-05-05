dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

tdy = [0, 1, 0, -1]
tdx = [-1, 0, 1, 0]

ret = 0
def debug(_board):
    for b in _board:
        print(b)
    print()


def transform(_board, _n):
    _temp = []
    y, x, d = _n // 2, _n // 2, 0
    can, flag = 1, 2
    while not (y == 0 and x == 0):
        for i in range(flag):
            for j in range(can):
                y, x = y + tdy[d], x + tdx[d]
                _temp.append(_board[y][x])
            d = (d + 1) % 4
        can += 1
        if can >= n - 1:
            flag = 3
    while 0 in _temp:
        _temp.remove(0)
    _temp = _temp + [0] * ((_n ** 2 - 1) - len(_temp))
    return _temp


def inverse(_temp, _n):
    _ret = [[0] * _n for _ in range(_n)]
    y, x, d = _n // 2, _n // 2, 0
    can, flag, c = 1, 2, 0
    while not (y == 0 and x == 0):
        for i in range(flag):
            for j in range(can):
                y, x = y + tdy[d], x + tdx[d]
                _ret[y][x] = _temp[c]
                c += 1
            d = (d + 1) % 4
        can += 1
        if can >= n - 1:
            flag = 3
    return _ret


def move_marble(_board, _n):
    temp = transform(_board, _n)
    return inverse(temp, _n)


def bomb_marble(_board, _n):
    global ret
    temp = transform(_board, _n)
    idx = 0
    while idx < len(temp):
        tmp, cnt = idx, 0
        while tmp + 1 < len(temp) and temp[tmp] == temp[tmp + 1]:
            tmp, cnt = tmp + 1, cnt + 1
        if cnt >= 3:
            ret += temp[idx] * (cnt + 1)
            for j in range(idx, idx + cnt + 1):
                temp[j] = 0
            idx += cnt
        idx += 1
    return inverse(temp, _n)


def change_marble(_board, _n):
    temp = transform(_board, _n)
    idx = 0
    group = []
    while idx < len(temp) and temp[idx] != 0:
        tmp, cnt = idx, 0
        while tmp + 1 < len(temp) and temp[tmp] == temp[tmp + 1]:
            tmp, cnt = tmp + 1, cnt + 1
        group.append(cnt + 1)
        group.append(temp[idx])
        idx += cnt + 1
    group = group + [0] * ((_n ** 2 - 1) - len(group))
    return inverse(group, _n)


def do_magic(_board, sy, sx, d, s):
    for i in range(s):
        sy, sx = sy + dy[d - 1], sx + dx[d - 1]
        _board[sy][sx] = 0


def solution(_board, _magic, _n, _m):
    for test_case in magic:
        sy, sx = _n // 2, _n // 2
        d, s = map(int, test_case)
        do_magic(_board, sy, sx, d, s)
        _board = move_marble(_board, _n)
        while True:
            temp = _board.copy()
            _board = bomb_marble(_board, _n)
            if temp == _board:
                break
            _board = move_marble(_board, _n)
        _board = change_marble(_board, _n)
    print(ret)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    magic = [list(map(int, input().split())) for _ in range(m)]
    solution(board, magic, n, m)
