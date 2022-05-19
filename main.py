from collections import defaultdict
from typing import List
import graphviz
import random
import numpy as np
import time


class Vertix(object):

    def __init__(self, tag) -> None:
        self.tag = tag
        self.edges = []

    def add_edge(self, target) -> None:
        if target in self.edges:
            return
        self.edges.append(target)
    
class Graph:

    def __init__(self, num_vertices: int) -> None:
        self.vertices = [Vertix(i) for i in range(num_vertices)]


    def create(self) -> None:
        for vertix in self.vertices:
            random.seed(time.clock())
            num_edges = random.randint(1, len(self.vertices) - 1)
            vertices_available = [vertix_available for vertix_available in self.vertices if vertix_available.tag != vertix.tag]
            targets = random.sample(population=vertices_available, k=num_edges)
            for target in targets:
                vertix.add_edge(target)
                target.add_edge(vertix)

    def get_vertices_from_tags(self, tags: list) -> List[Vertix]:
        result = []
        for vertix in self.vertices:
            is_there = len([tag for tag in tags if tag == vertix.tag]) > 0
            if is_there:
                result.append(vertix)
            
        return result

    def get_vertices_tag(self) -> List[str]:
        return [vertix.tag for vertix in self.vertices]


graph = Graph(num_vertices=5)
graph.create()

gviz = graphviz.Graph('finite_state_machine', filename='fsm.gv')
gviz.attr(rankdir='LR', size='8,5')
gviz.attr('node', shape='circle')


for vertix in graph.vertices:
    for target in vertix.edges:
        gviz.edge(f'{vertix.tag}', f'{target.tag}', label=f'E{vertix.tag}-{target.tag}')

gviz.render(directory='doctest-output', view=True)

