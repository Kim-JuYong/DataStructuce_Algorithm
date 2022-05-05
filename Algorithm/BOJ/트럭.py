

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))


def move(bridge, W):
    cnt = 0
    for i in range(len(bridge)):
        bridge[i][0] += 1
        if bridge[i][0] > W:
            cnt += 1
    for i in range(cnt):
        bridge.pop(0)


def solution():
    bridge, cnt = [], 0
    while True:
        cnt += 1
        move(bridge, W)
        if len(trucks) == 0 and len(bridge) == 0:
            print(cnt)
            break
        if len(trucks) > 0:
            weight = sum([b[1] for b in bridge]) + trucks[0]
            if len(bridge) <= W and weight <= L:
                bridge.append([1, trucks[0]])
                trucks.pop(0)


solution()
