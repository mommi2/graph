import graphviz
import random
import numpy as np


digraph_dict = np.zeros((5, 5), dtype=np.int8)
n_cols, n_rows = digraph_dict.shape

for j in range(n_rows):
    for i in range(n_cols):
        edge_rnd = random.randint(0, 1)
        digraph_dict[j][i] = digraph_dict[i][j] = edge_rnd


print(digraph_dict)


# f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
# f.attr(rankdir='LR', size='8,5')

# f.attr('node', shape='doublecircle')
# f.node('LR_0')
# f.node('LR_3')
# f.node('LR_4')
# f.node('LR_8')

# f.attr('node', shape='circle')
# f.edge('LR_0', 'LR_2', label='SS(B)')
# f.edge('LR_0', 'LR_1', label='SS(S)')
# f.edge('LR_1', 'LR_3', label='S($end)')
# f.edge('LR_2', 'LR_6', label='SS(b)')
# f.edge('LR_2', 'LR_5', label='SS(a)')
# f.edge('LR_2', 'LR_4', label='S(A)')
# f.edge('LR_5', 'LR_7', label='S(b)')
# f.edge('LR_5', 'LR_5', label='S(a)')
# f.edge('LR_6', 'LR_6', label='S(b)')
# f.edge('LR_6', 'LR_5', label='S(a)')
# f.edge('LR_7', 'LR_8', label='S(b)')
# f.edge('LR_7', 'LR_5', label='S(a)')
# f.edge('LR_8', 'LR_6', label='S(b)')
# f.edge('LR_8', 'LR_5', label='S(a)')

# f.render(directory='doctest-output', view=True)

