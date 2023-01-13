import sys

sys.stdin = open("/Users/juyong/Desktop/DataStructure_Algorithm/Algorithm/SAMSUNG/sample_input.txt", "r")


def solution(N, heights):
    max_height = max(heights)
    need_height = [max_height - h for h in heights if h != max_height]  # 나무가 자라야 하는 높이
    sum_need_height = sum(need_height)  # 총 필요한 높이

    need_odd_day = len([h for h in need_height if h % 2 == 1])  # 홀수 만큼 자라는 나무는 홀수 날에 꼭 물을 1번 줘야함
    min_day = need_odd_day * 2 - 1  # 그래서 최소 필요한 날을 구할 수 있음
    max_day = sum_need_height * 2 - 1  # 홀수 날에만 물을 줘서 만족하는 경우가 최대로 필요한 날임

    for day in range(min_day, max_day + 1):  # 최소 필요헌 날 ~ 최대 날짜 사이에 답이 있을 것
        # 3일엔 짝수날 1번 홀수날 2번 , 4일엔 짝수날 2번 홀수날 2번
        even_day = day // 2
        if day % 2 == 0:
            odd_day = even_day
        else:
            odd_day = even_day + 1
        # 짝수 날에 높이 2 홀수 날은 높이 1 이 자란다. 이 합이 "모든 나무가 자라야 할 총 높이" 보다 크거나 같으면 조건 만족
        if even_day * 2 + odd_day * 1 >= sum_need_height:
            return day
        # 왜 같을 때만이 아니라 크거나 같다 일까?? -> 물을 안줘도 되는 경우가 있기 때문! 자라야 할 높이 보다 오버 되면 물을 어느 날에 안주면 만족!!
    return 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))
    answer = solution(N, heights)
    print(f"#{test_case}", answer)
