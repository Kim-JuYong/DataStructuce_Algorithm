def log(n):
    ret, cnt = 1, 1
    if n == 1:
        return 1
    while ret < n:
        ret *= 2
        cnt += 1
    return cnt

def solution(n, a, b):
    answer = 0

    sub = abs(a-b)
    if (a <= n // 2 and b > n // 2) or (b <= n // 2 and a > n // 2):
        return log(n) - 1
    
    answer = log(sub)
    print(answer)
    return answer

solution(16, 4 , 6)