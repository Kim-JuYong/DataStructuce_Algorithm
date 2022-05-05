import sys

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]


def move_cloud(_cloud, d_i, s_i, _n):
    dy_i, dx_i = s_i * dy[d_i-1], s_i * dx[d_i-1]
    for c in _cloud:
        c[0] = (c[0] + dy_i) % _n
        c[1] = (c[1] + dx_i) % _n
    return _cloud


def rainy(_cloud, _board, _n):
    for c in _cloud:
        _board[c[0]][c[1]] += 1
    return _board


def water_copy(_cloud, _board, _n):
    for c in _cloud:
        y, x = c[0], c[1]
        for i in range(1, 8, 2):
            next_y, next_x = y + dy[i], x + dx[i]
            if -1 < next_y < _n and -1 < next_x < _n and board[next_y][next_x] > 0:
                _board[y][x] += 1
    return _board


def make_cloud(_cloud, _board, _n):
    new_cloud = []
    cloud_board = [([0] * _n) for j in range(_n)]
    for c in _cloud:
        cloud_board[c[0]][c[1]] = 1
    for i in range(_n):
        for j in range(_n):
            if _board[i][j] >= 2 and cloud_board[i][j] == 0:
                new_cloud.append([i, j])
                _board[i][j] -= 2
    return _board, new_cloud


def solution(_n, _m, _board, _move_info):
    cloud = [[_n-1, 0], [_n-1, 1], [_n-2, 0], [_n-2, 1]]
    for i in range(_m):
        # 1
        d_i, s_i = _move_info[i][0], _move_info[i][1]
        cloud = move_cloud(cloud, d_i, s_i, _n)
        # 2
        _board = rainy(cloud, _board, _n)
        # 4
        _board = water_copy(cloud, _board, _n)
        # 5 + 3
        _board, cloud = make_cloud(cloud, _board, _n)
    ret = 0
    for i in range(_n):
        for j in range(_n):
            ret += _board[i][j]
    print(ret)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().rstrip().split())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    move_info = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
    solution(n, m, board, move_info)

