n, q = input().split()
n = int(n)
q = int(q)

dict_node_parent = {}
dict_node_child_num = {}

list_input_n = list(map(int, input().split()))

# tree = BST()
# pre-process
for i in range(0, n - 1):
    dict_node_child_num[list_input_n[i]] = dict_node_child_num.get(list_input_n[i], 0) + 1
    dict_node_parent[i + 2] = list_input_n[i]

list_ans = []

for i in range(q):
    input_s_list = list(map(int, input().split()))  # can be improved (set)
    n_s = input_s_list[0]
    input_s_list.pop(0)  # can be slightly improved
    input_s_list = set(input_s_list)
    ans = 0
    for node_khat_j in input_s_list:
        parent = 0
        if dict_node_parent.get(node_khat_j, -1) in input_s_list:  # can be improved
            parent = 1
        ans += dict_node_child_num.get(node_khat_j, 0) + 1 - 2*parent
    list_ans.append(ans)

print(*list_ans, sep='\n')
