import itertools
import copy

def calculate(num1, num2, operator):
    if operator == '+':
        return int(num1) + int(num2)
    if operator == '-':
        return int(num1) - int(num2)
    if operator == '*':
        return int(num1) * int(num2)

def solution(expression: str):
    answer = 0
    operators = [a for a in expression if a in '+-*']
    expression = expression.replace('+', ',').replace('-', ',').replace('*', ',').split(',')
    for i in range(len(operators)):
        expression.insert(i*2 + 1, operators[i])

    operators = set(operators)
    priorities = list(itertools.permutations(operators, len(operators)))
    
    for operator in priorities:
        temp = copy.deepcopy(expression)
        for cur in operator:
            while cur in temp:
                idx = temp.index(cur)
                temp[idx] = calculate(temp[idx - 1], temp[idx + 1], temp[idx])
                del temp[idx-1]
                del temp[idx]

        answer = max(answer, abs(temp[-1]))
    return answer

if __name__ == '__main__':
    solution("100-200*300-500+20")
