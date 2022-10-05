# - 공간 넓이 = N*N (5<=N<=15)
# - 파리채 넓이 = M*M (2<=M<=N)
# - 각 영역 내 숫자 = 파리 수 (최대 30)
# 테스트 케이스 백 개 : 2초

# import sys
# sys.stdin = open("sample_input.txt", "r")

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def recursive(_board, _n, cur_y, cur_x, cur_d):
    cnt = 0
    while True:
        cur_y, cur_x = cur_y + dy[cur_d], cur_x + dx[cur_d]
        if -1 < cur_y < n and -1 < cur_x < n and _board[cur_y][cur_x] == 'o':
            cnt += 1
        else:
            return False

        if cnt == 2:
            return True
        

def soultion(_n, _board) -> str:
    for y in range(_n):
        for x in range(_n):
            if _board[y][x] == 'o': # 돌이 있으면 
                for d in range(8):  # 8 방향을 탐색해서
                    next_y, next_x = y + dy[d], x + dx[d] 
                    if -1 < next_y < n and -1 < next_x < n and board[next_y][next_x] == 'o': # 8방향에 범위 안이고 돌이 있으면
                        if recursive(next_y, next_x, d): # 체크
                            return "YES"
    return "NO"


t_c = int(input())

for c in range(t_c):
    n = int(input())
    board = [list(input()) for i in range(n)]
    answer = soultion(n, board)
    print("#" + str(c + 1), answer)
