import sys

n, m, k = 0, 0, 0
board = []
current = []
priority = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dd = {(0, -1): 3, (0, 1): 4, (-1, 0): 1, (1, 0): 2}
order_dict = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}


def spread(visit):
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                visit[i][j] = [board[i][j], k]


def decrease(visit):
    for i in range(n):
        for j in range(n):
            if visit[i][j][1] > 0:
                visit[i][j][1] -= 1
            if visit[i][j][1] == 0:
                visit[i][j] = [0, 0]


def solution():
    sharks = [(i, j, board[i][j]) for i in range(n) for j in range(n) if board[i][j] > 0]
    sharks.sort(key=lambda x: -x[2])  # 번호가 큰 상어 부터 순차적 이동
    visit = [[[0, 0] for i in range(n)] for j in range(n)]  # [냄새 뿌린 상어 번호, 냄새 지속 시간]
    spread(visit)
    count = 0
    while count <= 1000:
        if len(sharks) == 1:
            return count
        for shark in sharks:  # 번호가 큰 상어 부터 순차적 이동
            y, x, shark_num = shark[0], shark[1], shark[2]
            prior = priority[shark_num - 1][current[shark_num - 1] - 1]
            orders = [order_dict[p] for p in prior]
            find_blank = False
            for o in orders:  # 방향 우선 순위로 탐색
                next_y, next_x = y + o[0], x + o[1]
                if -1 < next_y < n and -1 < next_x < n:
                    if visit[next_y][next_x] == [0, 0]:  # 빈 칸으로 바로 이동 후 방향 전환
                        board[y][x], board[next_y][next_x] = 0, shark_num
                        current[shark_num - 1] = dd[(o[0], o[1])]
                        find_blank = True
                        break
            if not find_blank:  # 빈 칸이 없어서 자기 냄새로 돌아감
                for o in orders:  # 우선 순위로 탐색
                    next_y, next_x = y + o[0], x + o[1]
                    if -1 < next_y < n and -1 < next_x < n:
                        if visit[next_y][next_x][0] == shark_num:  # 자신의 냄새가 있는 칸으로 바로 이동 후 방향 전환
                            board[y][x], board[next_y][next_x] = 0, shark_num
                            current[shark_num - 1] = dd[(o[0], o[1])]
                            break
        sharks = [(i, j, board[i][j]) for i in range(n) for j in range(n) if board[i][j] > 0]  # 현재 상어 위치 최신화
        sharks.sort(key=lambda x: -x[2])
        decrease(visit)  # 냄새 -1
        spread(visit)  # 냄새 확산
        count += 1
    return -1


if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
    current = list(map(int, sys.stdin.readline().rstrip().split()))
    priority = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(4 * m)]
    priority = [priority[i: i + 4] for i in range(0, 4 * m, 4)]
    print(solution())
