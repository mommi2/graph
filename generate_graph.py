from collections import defaultdict
from typing import List
import graphviz
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
from collections import deque
import time

from graph import Graph


NUM_VERTICES = 500
GAMMA_OFFSET = 0
GAMMA_SHAPE = 2
GAMMA_SCALE = 2

LINSPACE_MARGIN_RIGHT = 2

total_time_execution = 0


def log_time_execution(msg, time_execution):
    global total_time_execution
    total_time_execution += time_execution
    print(f'{msg}: {time_execution}s')


start_time = time.time()
graph = Graph(NUM_VERTICES, gamma_shape=GAMMA_SHAPE, gamma_offset=GAMMA_OFFSET, gamma_scale=GAMMA_SCALE)
distr_edges = graph.create()

log_time_execution('Creazione grafo', time.time() - start_time)

start_time = time.time()
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
log_time_execution('Visualizzazione grafo', time.time() - start_time)

start_time = time.time()
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = gamma.stats(GAMMA_SHAPE, moments='mvsk')
x = np.linspace(0, max(distr_edges) + LINSPACE_MARGIN_RIGHT)
ax.plot(x, gamma.pdf(x, GAMMA_SHAPE, scale=GAMMA_SCALE), 'r-', label=f'gamma pdf con shape={GAMMA_SHAPE}, scale={GAMMA_SCALE}')
ax.hist(distr_edges, density=True, histtype='stepfilled', label='distr. numero edge')
ax.legend(loc='best', frameon=False)
log_time_execution('Creazione plot', time.time() - start_time)
print(f'Total time execution: {total_time_execution}s')
plt.show()

