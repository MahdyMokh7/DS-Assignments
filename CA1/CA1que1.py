
dict_all_states = dict()
dict_bin_each_char = dict()
state = 0  # int 0 to 1023
alphabet = 'abcdefghij'


def init():
    global dict_all_states
    global dict_bin_each_char
    dict_bin_each_char = {alphabet[i]: 1 << i for i in range(len(alphabet))}
    dict_all_states = {i: 0 for i in range(2 ** len(alphabet))}


if __name__ == '__main__':
    line_str = input()
    init()
    dict_all_states[0] = 1
    ans = 0
    for char in line_str:
        # state: int (binary 10bits) 1:char has came odd times, 0:char has came even times
        state = dict_bin_each_char[char] ^ state
        dict_all_states[state] += 1
        for char_alph in alphabet:
            state_temp = state ^ dict_bin_each_char[char_alph]
            ans += dict_all_states[state_temp]  # one odd
        if dict_all_states[state] >= 2:  # all even
            ans += dict_all_states[state] - 1
    print(ans)
