# import pdb
from math import ceil


def binary_search(l, r, key):
    mid = ceil((l + r) / 2)
    if r - l <= 1:
        if stack[l] == key:
            return l
        elif stack[r] == key:
            return r
        else:
            if key < stack[l]:
                return l
            elif key < stack[r]:
                return r
            else:
                return -1

    if stack[mid] == key:
        return mid
    elif stack[mid] > key:
        return binary_search(l, mid, key)
    else:
        return binary_search(mid, r, key)


data = []
list_ans = []

n, d = list(map(int, input().split()))

for i in range(n):
    a, t, s = input().split()
    data.append((int(a), int(t), int(s)))

data.sort(key=lambda x: x[2], reverse=True)
stack = [i + 1 for i in range(d)]  # days

# pdb.set_trace()
total_cost = 0
flag_empty = False
for i in range(n):  # teachers
    # pdb.set_trace()
    start_day_i, num_days_i, cost_i = data[i]
    if len(stack) == 0:
        flag_empty = True
        total_cost += num_days_i * cost_i

    if not flag_empty:
        index_stack_start = binary_search(0, len(stack) - 1, start_day_i)  # you can reduce it
        if index_stack_start == -1:
            total_cost += num_days_i * cost_i
        elif len(stack) - index_stack_start >= num_days_i:
            stack = stack[0:index_stack_start] + stack[index_stack_start + num_days_i:]  # check this to timing
        else:
            total_cost += (num_days_i - (len(stack) - index_stack_start)) * cost_i
            stack = stack[0:index_stack_start]

print(total_cost)
