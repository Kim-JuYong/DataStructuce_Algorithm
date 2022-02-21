from itertools import combinations


def possible(n):
    ret = []
    for i in range(1, n + 1):
        ret += list(combinations(range(n), i))
    return ret


def uniqueness(relation, columns):
    temp = set()
    for i in range(len(relation)):  # columns들의 조합으로 key를 만들고 set에 저장
        t = ''
        for j in columns:
            t += relation[i][j]
        temp.add(t)
    if len(temp) == len(relation):  # set 길이가 relation 길이와 같다면 이는 유일성을 만족한 것임
        return True
    return False


def minimality(unique_keys):
    unique_keys = [list(r) for r in unique_keys]
    ret = []
    for i in range(len(unique_keys)):  # key 이루는 column 수가 작은 순으로
        flag = True
        for j in range(len(ret)):  # 만약 지금 확인 중인 column 조합이 이미 최소성을 인정 받는 키의 모집합이라면 최소성 만족x
            intersection = list(set(unique_keys[i]) & set(ret[j]))
            if len(intersection) == len(ret[j]):
                flag = False
        if flag:
            ret.append(unique_keys[i])
    return len(ret)


def solution(relation):
    answer = 0
    combination = possible(len(relation[0]))  # 가능한 column 의 조합
    unique_keys = []
    for columns in combination:
        if uniqueness(relation, columns):  # 유일성 확인
            unique_keys.append(columns)
    answer = minimality(unique_keys)  # 최소성 확인
    return answer


if __name__ == '__main__':
    solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
              ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])

