import sys
import collections

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def rotate_90(_part_board):
    return list(map(list, zip(*_part_board[::-1])))


def divide_board(_board, _n, _l):
    ret = [[] for _ in range(_n)]
    for i in range(0, _n, _l):
        for j in range(0, _n, _l):
            part_board = []
            for k in range(0, _l):
                part_board.append(_board[i + k][j: j + _l])
            rotated = rotate_90(part_board)
            for k in range(0, _l):
                ret[i+k] += rotated[k]
    return ret


def melt_check(_board, _y, _x, _n):
    ret = 0
    for i in range(4):
        ny, nx = _y + dy[i], _x + dx[i]
        if -1 < ny < _n and -1 < nx < _n:
            if _board[ny][nx] > 0:
                ret += 1
    if ret < 3:
        return True
    return False


def melt_ice(_board, _n):
    ret = [[0] * _n for _ in range(_n)]
    for i in range(_n):
        for j in range(_n):
            if _board[i][j] > 0 and melt_check(_board, i, j, _n):
                ret[i][j] = _board[i][j] - 1
            else:
                ret[i][j] = _board[i][j]
    if ret == 1:
        return 0
    return ret


def bfs(_board, _y, _x, _n):

    q, ret = collections.deque(), 1
    q.append([_y, _x])
    visit = [[0] * _n for _ in range(_n)]
    visit[_y][_x] = 1

    while len(q) != 0:
        cur_y, cur_x = map(int, q.popleft())
        for i in range(4):
            ny, nx = cur_y + dy[i], cur_x + dx[i]
            if -1 < ny < _n and -1 < nx < _n:
                if _board[ny][nx] > 0 and visit[ny][nx] == 0:
                    q.append([ny, nx])
                    visit[ny][nx] = 1
                    ret += 1
    return ret


def solution(_board, _l,  _n, _q):
    sum_ice = 0
    max_ice = 0
    for order in _l:
        _board = divide_board(_board, 2**_n, 2**order)
        _board = melt_ice(_board, 2**_n)

    for i in range(2**_n):
        for j in range(2**_n):
            sum_ice += _board[i][j]
            if _board[i][j] > 0:
                max_ice = max(max_ice, bfs(_board, i, j, 2**_n))

    print(sum_ice)
    print(max_ice)


if __name__ == '__main__':
    n, q = map(int, sys.stdin.readline().rstrip().split())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2**n)]
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(board, l, n, q)