import collections
import copy
import itertools
import math
import sys

dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]


def bfs(_n: int, _m: int, _board: list) -> int:
    ret = 0
    q = [(i, j) for i in range(_n) for j in range(_m) if _board[i][j] == 2]
    while len(q) != 0:  # 바이러스 확산
        y, x = q[0][0], q[0][1]
        q.pop(0)
        for i in range(4):
            next_y, next_x = y + dy[i], x + dx[i]
            if -1 < next_y < _n and -1 < next_x < _m:
                if _board[next_y][next_x] == 0:
                    q.insert(0, (next_y, next_x))
                    _board[next_y][next_x] = 2
    for i in range(_n):  # 안전 영역 카운트
        for j in range(_m):
            if _board[i][j] == 0:
                ret += 1
    return ret


def solution(_n: int, _m: int, _board: list) -> int:
    answer = 0
    safe_zone = [(i, j) for i in range(_n) for j in range(_m) if _board[i][j] == 0]
    can_build_zone = list(itertools.combinations(safe_zone, 3))  # 벽 3개를 세울 수 있는 경우의 수
    for can_points in can_build_zone:
        temp = copy.deepcopy(board)
        for point in can_points:  # 벽 3개 세우기
            temp[point[0]][point[1]] = 1
        answer = max(answer, bfs(_n, _m, temp))
    return answer


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().rstrip().split())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
    print(solution(n, m, board))
