import sys


def solution(N, stages):
    answer = []
    challenge = [0 for i in range(N + 2)]
    failure = [0 for i in range(N + 2)]
    for stage in stages:
        challenge[stage] += 1
    for i in range(1, N + 1):
        try:
            failure[i] = challenge[i] / sum(challenge[i:])
        except ZeroDivisionError:
            failure[i] = 0
            continue

    for i, v in enumerate(failure):
        failure[i] = [v, i]
    failure.pop(0)
    failure.sort(key=lambda x: (x[0], -x[1]))
    answer = [failure[i][1] for i in range(len(failure) - 1, 0, -1)]

    return answer


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b, c = map(int, sys.stdin.readline().rstrip().split())
    solution(n, a, b, c)
