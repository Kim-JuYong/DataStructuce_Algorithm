

def transform_user_id(user_id, b):
    can_id = [u for u in user_id if len(u) == len(b)]
    star = [i for i in range(len(b)) if b[i] == '*']
    ret = []
    for i in range(len(can_id)):
        temp = can_id[i]
        for j in star:
            temp = temp[:j] + '*' + temp[j+1:]
        if temp == b:
            ret.append(can_id[i])
    return ret


def solution(user_id, banned_id):
    answer = 1
    can = []
    for b in banned_id:
        can.append(transform_user_id(user_id, b))
    for i in range(len(can)):
        for j in r
    return answer

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])