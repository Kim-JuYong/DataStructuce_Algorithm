def solution(new_id):
    answer = ''
    # step 1, 2
    new_id = ''.join([s for s in new_id.lower() if s.isalnum() or s == '-' or s == '_' or s == '.'])
    # step 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # step 4
    new_id = new_id.strip('.')
    # step 5
    if new_id == '':
        new_id += 'a'
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[0: 15]
    new_id = new_id.rstrip('.')
    # step 7
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3 - len(new_id))
    answer = new_id

    return answer


if __name__ == '__main__':
    solution("abcdefghijklmn.p")