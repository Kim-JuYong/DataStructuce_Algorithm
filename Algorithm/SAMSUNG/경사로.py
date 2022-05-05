import sys

def check(n, l, line):
    same, c = 1, 0
    while c < n -1 :
        if line[c] == line[c+1]:    # 높이가 같을 때
            same += 1
        elif line[c] + 1 == line[c+1] and same >= l:    # 높이가 1 높을 때
            same = 1    
        elif line[c] - 1 == line[c+1]:    # 높이가 1 낮을 때
            for i in range(1, l):   # 현재 블록 다음 l 개의 블록의 높이가 같아야 함
                if c + i + 1 >= n or line[c + i] != line[c + i + 1]:    # 범위 벗어나거나 높이가 다르면 경사로 x
                    return False
            c, same = c + l - 1, 0  # c + l 블록으로 이동. 이동한 칸은 경사로 칸이므로 same = 0
        else:
            return False
        c += 1
        
    return True

def solution(n, l, board):
    lines = [board[i] for i in range(n)] + [[board[i][j] for i in range(n)] for j in range(n)]
    answer = 0
    for line in lines:
        if check(n, l, line):
            answer += 1
    print(answer)


if __name__ == '__main__':
    n, l = map(int, sys.stdin.readline().rstrip().split())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    solution(n, l, board)