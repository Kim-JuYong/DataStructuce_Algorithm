
def solution(s: str):
    answer = 0
    stack = []
    for i in range(len(s)):
        if len(stack) == 0 or stack[-1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) == 0:
        return 1

    return answer


solution("baabaa")
