


def solution(origin, command):
    for i  in range(len(commands)):
        if commands[i] == 'I':
            x, y = int(commands[i+1]), int(commands[i+2])
            s = commands[i+3: i+3+y]
            origin = origin[:x+1] + s + origin[x+1:]
        elif commands[i] == 'D':
            x, y = int(commands[i+1]), int(commands[i+2])
            origin = origin[:x+1] + origin[x+y+1:]
        elif commands[i] == 'A':
            y = int(commands[i+1])
            s = commands[i+2: i+2+y] 
            origin = origin + s
    return ' '.join(origin[1:11])

for test_case in range(1, 11):
    n = int(input())
    origin = input().split()
    k = int(input())
    commands = input().split()
    origin.append('0') # index 맞춰주려공
    print(f'#{test_case}', solution(origin.copy(), commands))




