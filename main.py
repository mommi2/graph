from collections import defaultdict
import graphviz
import random
import numpy as np


graph_matrix = np.zeros((5, 5), dtype=np.int8)
n, m = graph_matrix.shape

for j in range(m):
    for i in range(n):
        rnd_result = random.randint(0, 1)
        graph_matrix[j][i] = graph_matrix[i][j] = rnd_result

print(graph_matrix)

gviz = graphviz.Graph('finite_state_machine', filename='fsm.gv')
gviz.attr(rankdir='LR', size='8,5')
gviz.attr('node', shape='circle')

for j in range(m):
    for i in range(n):
        if graph_matrix[j][i] == 1:
            gviz.edge(f'{j}', f'{i}', label=f'L{j}{i}')

gviz.render(directory='doctest-output', view=True)

