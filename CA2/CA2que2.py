# input
n = int(input())
random_seq = tuple(map(int, input().split(' ')))

# pre-process
pos = {}
for i in range(len(random_seq)):
    pos[random_seq[i]] = i + 1

# algorithm requirements
stack1 = []
prv = {}
stack2 = []
ans = set()

# part1 finding the prvs
def find_prvs():
    for y in range(n, 0, -1):  # y is the value (not the position)
        while True:
            if len(stack1) == 0:
                prv[pos[y]] = -1
                break
            else:
                if stack1[-1] < pos[y]:
                    prv[pos[y]] = stack1[-1]
                    break
                else:
                    stack1.pop()

        stack1.append(pos[y])

find_prvs()
# print(prv)
# print(pos)
# print(random_seq)
# part2 finding the ans

def give_ans():
    print(0)
    for x in range(1, n + 1):
        while True:
            if stack2 and stack2[-1] > pos[x]:
                if random_seq[stack2[-1] - 1] in ans:
                    ans.remove(random_seq[stack2[-1] - 1])
                stack2.pop()
            else:
                if prv[pos[x]] != -1:
                    if len(stack2) == 0 or prv[pos[x]] != prv[stack2[-1]]:
                        ans.add(x)
                break

        stack2.append(pos[x])
        print(len(ans))


give_ans()
