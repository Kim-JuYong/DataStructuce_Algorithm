import sys
import copy


shark, shark_direct = [0, 0], 0
dd = {1: [-1, 0], 2: [-1, -1], 3: [0, -1], 4: [1, -1], 5: [1, 0], 6: [1, 1], 7: [0, 1], 8: [-1, 1]}
answer = 0
def where_fish(board, num):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == num:
                return [i, j]


def move_fish(board, shark_y, shark_x):
    fish = [board[i][j][0] for i in range(4) for j in range(4) if 1 <= board[i][j][0] <= 16]
    fish.sort()
    
    while len(fish) > 0:
        cur = where_fish(board, fish.pop(0))
        cur_y, cur_x = cur[0], cur[1]
        cur_d = board[cur_y][cur_x][1]
        for i in range(8):
            next_y, next_x = cur_y + dd[cur_d][0], cur_x + dd[cur_d][1]
            if -1 < next_y < 4 and -1 < next_x < 4 and not (next_y == shark_y and next_x == shark_x): #범위 안이고
                if not (next_y == shark_y and next_x == shark_x):
                    board[cur_y][cur_x][1] = cur_d
                    board[cur_y][cur_x], board[next_y][next_x] = board[next_y][next_x], board[cur_y][cur_x]
                    break
            cur_d += 1 # 방향 전환
            if cur_d == 9: cur_d = 1 
            

def shark_can_go(board, y, x, d):
    ret = []
    for i in range(1, 4):
        next_y, next_x = y + dd[d][0], x + dd[d][1]
        if -1 < next_y < 4 and -1 < next_x < 4:
            if 1 <= board[next_y][next_x][0] <= 16:
                ret.append([next_y, next_x])
        y, x = next_y, next_x
    return ret


def dfs(board, y, x, ret):
    global answer
    board = copy.deepcopy(board)
    eat, board[y][x][0] = board[y][x][0], -1 # 상어 이동
    move_fish(board, y, x) # 물고기 이동
    can_go = shark_can_go(board, y, x, board[y][x][1]) # 먹을 수 있는 물고기 칸
    answer = max(answer, ret + eat)
    for go in can_go:
        dfs(board, go[0], go[1], ret + eat)


if __name__ == '__main__':
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(4)]
    board = [[board[i][j:j+2] for j in range(0, 8, 2)] for i in range(4)]
    dfs(board, 0, 0, 0)
    print(answer)