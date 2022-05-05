
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


class Fireball:
    y = x = m = d = s = 0

    def __init__(self, _y, _x, _m, _s, _d):
        self.y, self.x = _y, _x
        self.m, self.d, self.s = _m, _d, _s


def move_fireball(_board, _n):
    ret = [[[] for _ in range(_n)] for _ in range(_n)]
    for i in range(_n):
        for j in range(_n):
            if len(_board[i][j]) > 0:
                for k in range(len(_board[i][j])):
                    cur = _board[i][j].pop(0)
                    cur.y, cur.x = (cur.y + (dy[cur.d] * cur.s)) % _n, (cur.x + (dx[cur.d] * cur.s)) % _n
                    ret[cur.y][cur.x].append(cur)
    return ret


def is_odd_even(sum_d):
    flag = sum_d[0] % 2
    for i in range(1, len(sum_d)):
        if flag != (sum_d[i] % 2):
            return False
    return True


def step2(_board, _n):
    for i in range(_n):
        for j in range(_n):
            if len(_board[i][j]) >= 2:
                sum_m, sum_s, sum_d = 0, 0, []
                for k in range(len(_board[i][j])):
                    sum_m += _board[i][j][k].m
                    sum_s += _board[i][j][k].s
                    sum_d.append(_board[i][j][k].d)
                new_m, new_s, new = sum_m // 5, sum_s // len(_board[i][j]), []
                if new_m != 0 and is_odd_even(sum_d):
                    for new_d in range(0, 8, 2):
                        new.append(Fireball(i, j, new_m, new_s, new_d))
                elif new_m != 0 and not is_odd_even(sum_d):
                    for new_d in range(1, 9, 2):
                        new.append(Fireball(i, j, new_m, new_s, new_d))
                _board[i][j] = new
    return _board


def solution(_board, _informs, _n, _k):
    for i in range(_k):
        _board = move_fireball(_board, _n)
        _board = step2(_board, _n)
    ret = 0
    for i in range(_n):
        for j in range(_n):
            for k in range(len(_board[i][j])):
                ret += _board[i][j][k].m
    print(ret)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [[[] for _ in range(n)] for _ in range(n)]
    informs = []
    for i in range(m):
        y, x, m, s, d = map(int, input().split())
        fireball = Fireball(y-1, x-1, m, s, d)
        informs.append([y-1, x-1])
        board[y-1][x-1].append(fireball)
    solution(board, informs, n, k)

