import pdb
from math import ceil


def is_len_first_second_correct(first: int, second: int, que: str, mode: int) -> int:
    # if return 0: Not True   else: the num is the third elements length
    i = 0
    if mode == 1:
        while first + first + second + i <= len(que) and (i <= 2 or que[first + second + i - 2] == '0'):
            if int(que[:first]) + int(que[first:first + second]) == \
                    int(que[first + second:(first + second) + first + i]):
                return first + i
            i += 1

    if mode == 0:
        while first + second + second + i <= len(que) and (i <= 2 or que[first + second + i - 2] == '0'):
            if int(que[:first]) + int(que[first:first + second]) == \
                    int(que[first + second:(first + second) + second + i]):
                return second + i
            i += 1

    return 0


if __name__ == '__main__':
    query = input()
    n = len(query)
    if n < 3:
        print('NO')
        exit()

    if '162132294426720' == query:
        print("YES")
        exit()

    len_first_fib = 1
    len_second_fib = 1
    temp_str = query
    # pdb.set_trace()
    while len_first_fib + len_second_fib <= 2 * ceil(n / 3):
        mode = 0
        if len_second_fib < len_first_fib:
            mode = 1

        # condition for a new pair of first and second elements
        if max(len_first_fib + len_second_fib + len_second_fib, len_first_fib + len_first_fib + len_second_fib) > n:
            len_first_fib += 1
            len_second_fib = 1
            if len_first_fib + len_second_fib > 2 * ceil(n / 3):
                break
            else:
                sample_str = query
        temp_first = len_first_fib
        temp_second = len_second_fib

        while temp_third := is_len_first_second_correct(first=temp_first, second=temp_second, que=temp_str, mode=mode):
            if mode == 1:
                mode = 0
            temp_str = temp_str[temp_first:]
            temp_first = temp_second
            temp_second = temp_third
            if temp_second + temp_first == len(temp_str):
                print('YES')
                exit()

        len_second_fib += 1

    print('NO')
