import collections

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dd = [0, 1, 2, 3]
ret = float('inf')

def have_cost(y, x, cur_d, next_d):
    if y == 0 and x == 0:
        return 100
    if cur_d in [0, 2] and next_d in [0, 2]:
        return 100
    if cur_d in [1, 3] and next_d in [1, 3]:
        return 100
    return 500


def dfs(board, stack, visit, y, x, d, n):
    global ret
    stack.append([y, x])
    print(y, x)
    if y == n-1 and x == n-1:
        print(stack)
        ret = min(ret, visit[y][x])
        print(ret)
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if -1 < ny < n and -1 < nx < n:
            if board[ny][nx] == 0 and visit[ny][nx] == float('inf'):
                visit[ny][nx] = visit[y][x] + have_cost(y, x, d, i)
                dfs(board.copy(), stack.copy(), visit.copy(), ny, nx, i, n)
                visit[ny][nx] = float('inf')
    for v in visit:
        print(v)
    print()
    stack.pop()



def solution(board):
    answer = 0
    #answer = dfs(board)
    n = len(board)
    visit = [[float('inf')] * n for _ in range(n)]
    visit[0][0] = 100
    dfs(board, [], visit, 0, 0, -1, n)
    print(ret)
    return answer


solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
