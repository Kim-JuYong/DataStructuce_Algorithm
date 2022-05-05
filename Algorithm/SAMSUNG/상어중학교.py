import sys
import collections


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(N, y, x, board):    #블록 그룹 찾기
    ret = [[y, x]]
    q = collections.deque()
    q.append([y, x])
    visit = [[0] * N for _ in range(N)]
    color, rainbow_block, visit[y][x] = board[y][x], 0, 1
    
    while len(q) != 0:
        cur_y, cur_x =  map(int, q.popleft())
        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if  -1 < next_y < N and -1 < next_x < N and visit[next_y][next_x] == 0: 
                if board[next_y][next_x] == color or board[next_y][next_x] == 0:    #색깔이 같은 블록이거나 무지개 블록이면 확장
                    q.append([next_y, next_x])
                    ret.append([next_y, next_x])
                    visit[next_y][next_x] = 1
                    if board[next_y][next_x] == 0:  # 무지개 블럭
                        rainbow_block += 1
    return rainbow_block, ret


def find_standard_block(board, group):   # 기준 블록 찾기
    temp = [(g[0], g[1]) for g in group if board[g[0]][g[1]] > 0]
    temp = sorted(temp, key=lambda x:(x[0], x[1]))
    return temp[0][0], temp[0][1]


def find_max_group(N, board):   # 1번 조건을 만족하는 블록 그룹 찾기
    color_blocks = [(i, j) for i in range(N) for j in range(N) if board[i][j] > 0]  
    candidate_groups = collections.defaultdict(list)
    
    for color_block in color_blocks:
        rainbow_blocks, group = bfs(N, color_block[0], color_block[1], board)
        if group:
            stand_y, stand_x = map(int, find_standard_block(N, board, group))
            candidate_groups[(len(group), rainbow_blocks, stand_y, stand_x)].append(group) 
    if candidate_groups:
        ret = sorted(candidate_groups.items(),key=lambda x: (-x[0][0], -x[0][1], -x[0][2], -x[0][3]))[0][1][0]
        return ret
    return []
    

def find_gravity_idx(cur, line):    # 블록이 떨어질 위치 찾기
    for i in range(cur-1, -1, -1):
        if line[i] >= -1:
            return i + 1
    return 0    


def gravity(N, board):  # 중력 작용
    temp = [[board[i][j] for i in range(N-1, -1, -1)] for j in range(N)]
    for line in temp:
        for i in range(N):
            if line[i] >= 0:
                idx = find_gravity_idx(i, line)
                line[idx], line[i] = line[i], line[idx]
    temp = [[temp[i][j] for i in range(N)] for j in range(N-1, -1, -1)]
    return temp


def removeBlocks(N, board, remove_group):   # 블록 제거
    for block in remove_group:
        board[block[0]][block[1]] = -2


def rotated(board):    # 반 시계 90도 뒤집기
    return list(map(list, zip(*board)))[::-1]


def solution(N, board):
    answer = 0
    while True:
        max_group = find_max_group(N, board)
        if len(max_group) < 2:  # 찾은 블록 그룹의 길이가 2 미만 이면 break
            break
        answer += len(max_group) ** 2
        removeBlocks(N, board, max_group)
        board = gravity(N, board)
        board = rotated(board)
        board = gravity(N, board)
    print(answer)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    solution(N, board)
