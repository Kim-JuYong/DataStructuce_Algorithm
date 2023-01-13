import sys

sys.stdin = open("input.txt", "r")


def solution(_n, _m, _a, _b):
    ret = 0
    for i in range(0, _m - _n + 1):
        num = 0
        for j in range(_n):
            num += _a[j] * _b[i + j]
        ret = max(ret, num)
    return ret


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    answer = 0
    if n > m:
        answer = solution(m, n, b, a)
    else:
        answer = solution(n, m, a, b)
    print(f"#{test_case} {answer}")
