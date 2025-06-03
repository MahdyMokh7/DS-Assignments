import pdb

n = int(input())

stack_inp = []
stack_ans = []
dict_stack = {}
dict_stack2 = {}

# get input and pre-process  O(n)
for i in range(n):
    inp = int(input())
    stack_inp.append(inp)
    dict_stack[inp] = dict_stack.get(inp, []) + [i]

# pdb.set_trace()
# check the -1 state
for i in range(n):
    if stack_inp[i] == 0:
        stack_ans.append(0)
    elif len(dict_stack[stack_inp[i]]) > 1:
        if i == dict_stack[stack_inp[i]][0] or i == dict_stack[stack_inp[i]][-1]:
            if len(stack_ans) == 0:
                stack_ans.append(stack_inp[i])
            elif stack_ans[-1] != stack_inp[i]:
                stack_ans.append(stack_inp[i])
            else:
                stack_ans.pop()
        else:
            if len(stack_ans) != 0:
                if stack_ans[-1] != stack_inp[i]:
                    print(-1)
                    exit()

# pdb.set_trace()

if len(stack_ans) != 0 and stack_ans.count(0) != len(stack_ans):
    print(-1)
    exit()
else:
    stack_ans = []


for i in range(n):
    if stack_inp[i] == 0:
        pass
    elif len(dict_stack[stack_inp[i]]) > 1:
        if i == dict_stack[stack_inp[i]][0] or i == dict_stack[stack_inp[i]][-1]:
            stack_ans.append(stack_inp[i])
            dict_stack2[stack_inp[i]] = False

# pdb.set_trace()
if len(stack_ans) == 0:
    if stack_inp.count(0) == len(stack_inp):
        print(0)
        exit()
    else:
        print(1)
        exit()


maxx = []
ele_max = []
count = 0
for i in range(len(stack_ans)):
    x = stack_ans.pop()
    if dict_stack2[x] == False:
        count += 1
        dict_stack2[x] = True
    else:
        count -= 1

    maxx.append(count)
    ele_max.append(x)

max_int = max(maxx)

for i in range(len(maxx)):
    if max_int == maxx[i]:
        first_index = stack_inp.index(ele_max[i])
        last_index = len(stack_inp) - stack_inp[::-1].index(ele_max[i]) - 1
        if last_index - first_index > 1:
            if stack_inp[first_index:last_index].count(ele_max[i]) != last_index - first_index:
                # pdb.set_trace()
                max_int += 1
                break

print(max_int)

