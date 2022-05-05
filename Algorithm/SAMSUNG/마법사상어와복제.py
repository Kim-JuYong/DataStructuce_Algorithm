import copy
import sys

fdy = [0, -1, -1, -1, 0, 1, 1, 1]
fdx = [-1, -1, 0, 1, 1, 1, 0, -1]

sdy = [-1, 0, 1, 0]
sdx = [0, -1, 0, 1]


def move_fish(_inform, _smell_board, _sy, _sx):
    for i, fish in enumerate(_inform):
        for j in range(fish[2], fish[2] - 8, -1):
            nd = j % 8
            if j <= 0:
                nd = j + 8
            ny, nx = fish[0] + fdy[nd - 1], fish[1] + fdx[nd - 1]
            if 0 < ny < 5 and 0 < nx < 5:
                if not (ny == _sy and nx == _sx) and _smell_board[ny][nx] == 0:
                    _inform[i] = [ny, nx, nd]
                    break
    return _inform


def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for n in product(arr, r-1):
                yield [arr[i]] + n


def go(_board, _move, _sy, _sx):
    fish, visit = 0, [[0] * 5 for _ in range(5)]
    for dd in _move:
        nsy, nsx = _sy + sdy[dd - 1], _sx + sdx[dd - 1]
        if 0 < nsy < 5 and 0 < nsx < 5:
            _sy, _sx = nsy, nsx
            if visit[nsy][nsx] == 0:
                fish += len(_board[nsy][nsx])
            visit[nsy][nsx] = 1
        else:
            return -1
    return fish


def move_shark(_board, _smell_board, _sy, _sx):
    can_move = []
    for p in product([1, 2, 3, 4], 3):
        fish = go(_board, p, _sy, _sx)
        if fish >= 0:
            order = str(p[0]) + str(p[1]) + str(p[2])
            can_move.append(p + [fish] + [order])
    move = sorted(can_move, key=lambda x: (-x[3], x[4]))[0]

    for dd in move[:3]:
        nsy, nsx = _sy + sdy[dd - 1], _sx + sdx[dd - 1]
        if len(_board[nsy][nsx]) > 0:
            _board[nsy][nsx] = []
            _smell_board[nsy][nsx] = 2
        _sy, _sx = nsy, nsx
    return _sy, _sx


def remove_smell(_smell_board):
    for i in range(1, 5):
        for j in range(1, 5):
            if _smell_board[i][j] > 0:
                _smell_board[i][j] -= 1


def put_inform(_board):
    ret = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(len(_board[i][j])):
                ret.append(_board[i][j][k])
    return ret


def put_fish(_board, _inform):
    for fish in _inform:
        _board[fish[0]][fish[1]].append(fish)
    return _board


def solution(_inform, _sy, _sx, _m, _s):
    smell_board = [[0] * 5 for _ in range(5)]
    for i in range(_s):
        temp = copy.deepcopy(_inform)

        _inform = move_fish(_inform.copy(), smell_board.copy(), _sy, _sx)
        board = put_fish([[[] for _ in range(5)] for _ in range(5)], _inform)

        remove_smell(smell_board)
        _sy, _sx = move_shark(board, smell_board, _sy, _sx)

        board = put_fish(board.copy(), temp)
        _inform = put_inform(board)

    print(len(_inform))


if __name__ == '__main__':
    m, s = map(int, sys.stdin.readline().rstrip().split())
    inform = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
    sy, sx = map(int, sys.stdin.readline().rstrip().split())
    solution(inform, sy, sx, m, s)
