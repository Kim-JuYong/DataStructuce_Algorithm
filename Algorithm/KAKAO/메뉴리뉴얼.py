import collections
import sys
import itertools


def can_course_menu(can: str, orders: list) -> int:
    count = 0
    for order in orders:
        o, c = set(order), set(can)
        if c.issubset(o):
            count += 1
    return count


def combination(orders: list, course: int) -> list:
    ret = []
    for order in orders:
        for j in itertools.combinations(order, course):
            ret.append(j)
    return ret


def solution(orders, course):
    answer = []
    orders = [list(order) for order in orders]
    for c in course:
        ret = {}
        can_combination = combination(orders, c)
        for can in can_combination:
            can = ''.join(can)
            how = can_course_menu(can, orders)
            if how >= 2:
                ret[can] = how
        if len(ret) > 0:
            max_how = max(ret.values())
            answer.append([k for k, v in ret.items() if v == max_how])
    answer = sum(answer, [])
    ret = set()
    for a in answer:
        a = ''.join((sorted(a)))
        ret.add(a)
    answer = list(ret)
    answer.sort()
    return answer
