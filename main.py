from collections import defaultdict
from typing import List
import graphviz
import random
import numpy as np
import time
from scipy.stats import gamma
import matplotlib.pyplot as plt


class Vertix(object):

    def __init__(self, tag, edges: list = None) -> None:
        self.tag = tag
        self.edges = edges or []

    def add_edge(self, target) -> None:
        if target in self.edges:
            return
        self.edges.append(target)
    
class Graph:

    def __init__(self, num_vertices: int) -> None:
        self.vertices = [Vertix(i) for i in range(num_vertices)]


    def create(self):
        num = []
        for vertix in self.vertices:
            random.seed(time.process_time)
            rnd_value = int(gamma.rvs(2, loc=1))
            num.append(rnd_value)
            num_edges = len(self.vertices) - 1 if rnd_value > len(self.vertices) - 1 else rnd_value
            print(f'{vertix.tag} num edges: {num_edges}')
            vertices_available = [vertix_available for vertix_available in self.vertices if vertix_available.tag != vertix.tag]
            targets = random.sample(population=vertices_available, k=num_edges)
            for target in targets:
                vertix.add_edge(target)
                target.add_edge(vertix)
        return num
        

    def get_vertices_from_tags(self, tags: list) -> List[Vertix]:
        result = []
        for vertix in self.vertices:
            is_there = len([tag for tag in tags if tag == vertix.tag]) > 0
            if is_there:
                result.append(vertix)
            
        return result

    def get_vertices_tag(self) -> List[str]:
        return [vertix.tag for vertix in self.vertices]


fig, ax = plt.subplots(1, 1)
k = 2
mean, var, skew, kurt = gamma.stats(k, moments='mvsk')
x = np.linspace(1, 10, 100)
ax.plot(x, gamma.pdf(x, k), 'r-', lw=5, alpha=0.6, label='gamma pdf')

graph = Graph(num_vertices=20)
r = graph.create()

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

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

