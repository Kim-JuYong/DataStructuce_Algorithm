import sys
import collections

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


class Block:
    y = x = adj = none = 0

    def __init__(self, _y, _x, _adj, _none):
        self.y, self.x = _y, _x
        self.adj = _adj
        self.none = _none


def have_adj_and_none(_board, _like_who, cur_y, cur_x, _n):
    ret_adj, ret_none = 0, 0
    for i in range(4):
        adj_y, adj_x = cur_y + dy[i], cur_x + dx[i]
        if -1 < adj_y < _n and -1 < adj_x < _n:
            if _board[adj_y][adj_x] in _like_who:
                ret_adj += 1
            if _board[adj_y][adj_x] == 0:
                ret_none += 1

    return ret_adj, ret_none


def find_seat(_board, like_who, _n):
    can = []
    for i in range(_n):
        for j in range(_n):
            if _board[i][j] == 0:
                ret_adj, ret_none = have_adj_and_none(_board, like_who, i, j, _n)
                can.append(Block(i, j, ret_adj, ret_none))
    can = sorted(can, key=lambda x: (x.adj, x.none, -x.y, -x.x))
    return can[-1].y, can[-1].x


def solution(_board, _inform, _n):
    for k, v in _inform.items():
        y, x = find_seat(_board, v, _n)
        _board[y][x] = k
    ret = 0
    for i in range(_n):
        for j in range(_n):
            r, s = have_adj_and_none(_board, _inform[_board[i][j]], i, j, _n)
            if r >= 1:
                ret += 10 ** (r-1)
    print(ret)


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    board = [[0] * n for _ in range(n)]
    inform = collections.defaultdict(list)
    for _ in range(n*n):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        inform[line[0]] = line[1:]
    solution(board, inform, n)
