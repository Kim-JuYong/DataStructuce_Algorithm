import sys

def rotate(n, robot, board):    #회전 
    board.insert(0, board[-1])
    robot.insert(0, 0)  
    robot[n-1] = 0  #내리는 위치 로봇 내림
    return robot[:n], board[:n*2]


def move_robot(n, robot, board):    #로봇 이동
    for i in range(n-2, -1, -1):   
        if robot[i] == 1 and robot[i+1] == 0 and board[i+1] > 0:
            robot[i], robot[i+1] =  0, 1
            board[i+1] -= 1
    robot[n-1] = 0  #내리는 위치 로봇 내림
    


def solution(n, k, board):
    robot, answer = [0] * n, 1
    while True:
        robot, board = rotate(n, robot, board)
        move_robot(n, robot, board)
        if board[0] > 0:    #올리는 위치 로봇 올림
            robot[0], board[0] = 1, board[0] - 1
        if board.count(0) >= k:
            break
        answer += 1
    print(answer)


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().rstrip().split())
    board = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, k, board)
