def calc_pure_time(time: str, frmt: str) -> int:
    hour, mint = list(map(int, time.split(sep=':')))
    if frmt == 'AM':
        if hour == 12:
            hour = 0
    else:
        if not hour == 12:
            hour += 12
    pure_time = 60 * hour + mint
    return pure_time



if __name__ == '__main__':
    num_test_cases = int(input())

    # time format
    time_format = "%I:%M %p"  # Format string for AM/PM time

    for i in range(num_test_cases):
        p_time, p_format = input().split()

        # calculating pure time from origin
        timeP = calc_pure_time(p_time, p_format)

        num_of_friends = int(input())
        tup_answers = tuple()
        for j in range(num_of_friends):
            L_time, L_format, R_time, R_format = input().split()

            # Creating time objects
            timeL = calc_pure_time(L_time, L_format)
            timeR = calc_pure_time(R_time, R_format)

            if timeL <= timeP <= timeR:
                tup_answers += ('1',)
            else:
                tup_answers += ('0',)
        print(''.join(tup_answers))


