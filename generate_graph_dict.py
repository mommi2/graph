from collections import defaultdict
import graphviz
from graph import GraphDict

NUM_VERTICES = 20
MAX_EDGES = 3

graph = GraphDict(NUM_VERTICES, MAX_EDGES)
graph_matrix = graph.create()

n, _ = graph_matrix.shape

print(graph_matrix)

gviz = graphviz.Graph('finite_state_machine', filename='fsm.gv')
gviz.attr(rankdir='LR', size='8,5')
gviz.attr('node', shape='circle')

edges_visited = defaultdict(list)

for j in range(n):
    for i in range(n):
        if graph_matrix[j][i] == 1 and (not i in edges_visited[j] and not j in edges_visited[i]):
            gviz.edge(f'{j}', f'{i}', label=f'E{j}{i}')
            edges_visited[j].append(i)

gviz.render(directory='doctest-output', view=True)
