import copy

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
visit = [[0] * N for _ in range(N)]


def dfs(y, x):
    stack, ret = [[y, x]], []
    visit[y][x] = 1
    while len(stack) > 0:
        cy, cx = map(int, stack.pop())
        ret.append([cy, cx])
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if -1 < ny < N and -1 < nx < N and visit[ny][nx] == 0:
                if L <= abs(board[cy][cx] - board[ny][nx]) <= R:
                    stack.append([ny, nx])
                    visit[ny][nx] = 1
    return ret


def solution():
    global visit
    cnt = 0
    while True:
        groups, temp = [], copy.deepcopy(board)
        visit = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visit[i][j] == 0:
                    groups.append(dfs(i, j))
        for group in groups:
            people = sum([board[g[0]][g[1]] for g in group]) // len(group)
            for g in group:
                board[g[0]][g[1]] = people
        if board == temp:
            break
        cnt += 1
    print(cnt)


solution()
