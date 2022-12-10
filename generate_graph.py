from collections import defaultdict
from typing import List
import graphviz
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
from collections import deque

from graph import Graph


NUM_VERTICES = 20
GAMMA_OFFSET = 1
GAMMA_K = 2

graph = Graph(NUM_VERTICES, gamma_k=GAMMA_K, gamma_offset=GAMMA_OFFSET)
r = graph.create()

gviz = graphviz.Graph('finite_state_machine', filename='fsm.gv')
gviz.attr(rankdir='LR', size='8,5')
gviz.attr('node', shape='circle')

edges_visited = defaultdict(list)

for vertix in graph.vertices:
    for target in vertix.edges:
        if not target.tag in edges_visited[vertix.tag] and not vertix.tag in edges_visited[target.tag]:
            gviz.edge(f'{vertix.tag}', f'{target.tag}', label=f'E{vertix.tag}-{target.tag}')
            edges_visited[vertix.tag].append(target.tag)

gviz.render(directory='doctest-output', view=True)

fig, ax = plt.subplots(1, 1)
k = GAMMA_K
mean, var, skew, kurt = gamma.stats(k, moments='mvsk')
x = np.linspace(GAMMA_OFFSET, 10, 100)
ax.plot(x, gamma.pdf(x, k), 'r-', lw=5, alpha=0.6, label='gamma pdf')

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

