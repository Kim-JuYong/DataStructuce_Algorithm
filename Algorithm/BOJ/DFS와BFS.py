import sys
from queue import Queue

n, m, v = 0, 0, 0
adjacent_list = []
visit = [0] * 1001


def dfs(current: int):
    visit[current] = 1
    print(current, end=' ')
    for i in range(1, n + 1):
        if adjacent_list[current][i] and not visit[i]:
            dfs(i)


def bfs(current: int):
    q = Queue()
    q.put(current)
    visit[current] = 1
    while not q.empty():
        cur = q.get()
        print(cur, end=' ')
        for i in range(1, n + 1):
            if adjacent_list[cur][i] and not visit[i]:
                visit[i] = 1
                q.put(i)


if __name__ == '__main__':
    n, m, v = map(int, sys.stdin.readline().rstrip().split())
    adjacent_list = [[0] * 1001 for i in range(1001)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adjacent_list[a][b], adjacent_list[b][a] = 1, 1
    dfs(v)
    visit = [0] * 1001
    print()
    bfs(v)

