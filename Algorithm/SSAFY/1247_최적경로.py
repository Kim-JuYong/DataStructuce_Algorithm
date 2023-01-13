import sys
sys.stdin = open("input.txt", "r")

import itertools


def get_distance(cy, cx, ny, nx):
    return abs(cy - ny) + abs(cx - nx)


def get_distance_map(_points, _n):
    ret = [[0] * _n for _ in range(_n)]
    for i in range(_n-1):
        for j in range(i+1, _n):
            y, x = map(int, _points[i])
            ny, nx = map(int, _points[j])
            distance = get_distance(y, x, ny, nx)
            ret[i][j] = distance
            ret[j][i] = distance
    return ret


def solution(_points, _n):
    ret = float('inf')
    distance_map = get_distance_map(_points, _n)
    for can in itertools.permutations(range(2, _n)): # can: 고객 idx 순열
        move = [0] + list(can) + [1]
        sum_distance, flag = 0, 0
        for i in range(0, _n - 1):
            cur, _next = move[i], move[i+1]
            sum_distance += distance_map[cur][_next]
            if sum_distance >= ret:
                flag = 1
                break
        if not flag:
            ret = min(ret, sum_distance)
    return ret


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    points = list(map(int, input().split()))
    points = [[points[i], points[i + 1]] for i in range(0, N * 2 + 4, 2)]
    answer = solution(points, N + 2)
    print(f"#{test_case} {answer}")