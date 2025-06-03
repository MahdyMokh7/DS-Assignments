if __name__ == '__main__':
    string_main = input()
    list_substr = []
    my_max = 0
    now = 0
    for index, char in enumerate(string_main):
        if char not in list_substr:
            now += 1
            list_substr.append(char)
        else:
            list_substr.append(char)
            index_rm = list_substr.index(char)
            list_substr = list_substr[index_rm + 1:]
            my_max = max(now, my_max)
            now -= index_rm
    print(max(my_max, now))
