def getHeadIdx(name: str):
    head_idx, num_idx = 0, len(name)
    for idx in range(len(name)):
        if name[idx].isdigit():
            head_idx = idx
            break
    print(head_idx, len(name))
    cnt = 0
    for idx in range(head_idx, len(name)):
        if not name[idx].isdigit() or cnt >= 4:
            num_idx = idx
            break
        cnt += 1
    print(name[:head_idx], name[head_idx:num_idx])
    print(head_idx, num_idx)
    return head_idx, num_idx


def solution(files):
    answer = []
    arr = []
    for idx, var in enumerate(files):
        head_idx, num_idx = map(int, getHeadIdx(var))
        head, num = var[:head_idx+1], var[head_idx+1:num_idx+1]
        arr.append([head.lower(), int(num), idx])
    arr.sort(key=lambda x: (x[0], x[1], x[2]))
    answer = [files[var[2]] for var in arr]
    return answer

solution(["b dadakmd 2000"])