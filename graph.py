from collections import deque
from typing import List
from collections import defaultdict
from scipy.stats import gamma
import random
import time
import numpy as np

from vertix import Vertix

class Graph:

    def __init__(self, num_vertices: int, gamma_shape: float, gamma_offset: float, gamma_scale: float) -> None:
        self.vertices = [Vertix(i) for i in range(num_vertices)]
        self.gamma_shape = gamma_shape
        self.gamma_offset = gamma_offset
        self.gamma_scale = gamma_scale


    def create(self):
        num = []
        for i in range(len(self.vertices)):
            vertix = self.vertices[i]
            random.seed(time.process_time)
            rnd_value = int(gamma.rvs(self.gamma_shape, loc=self.gamma_offset, scale=self.gamma_scale))
            num.append(rnd_value)
            num_edges = len(self.vertices) - 1 if rnd_value > len(self.vertices) - 1 else rnd_value
            vertices_available = [vertix_available for vertix_available in self.vertices if vertix_available.tag != vertix.tag]
            targets = random.sample(population=vertices_available, k=num_edges)
            for target in targets:
                if i > 0 and self.is_reachable(self.vertices[i - 1].tag, target.tag):
                    vertix.add_edge(self.vertices[i - 1])
                    self.vertices[i - 1].add_edge(vertix)
                else:
                    vertix.add_edge(target)
                    target.add_edge(vertix)
                    
        return num
    
    def is_reachable(self, src, dest):
        # get the total number of nodes in the graph
        n = len(self.vertices)
    
        # to keep track of whether a vertex is discovered or not
        discovered = [False] * n
    
        # create a queue for doing BFS
        q = deque()
    
        # mark the source vertex as discovered
        discovered[src] = True
    
        # enqueue source vertex
        q.append(src)
    
        # loop till queue is empty
        while q:
    
            # dequeue front node and print it
            v = q.popleft()
    
            # if destination vertex is found
            if v == dest:
                return True
    
            # do for every edge (v, u)
            for u in self.get_vertix_from_tag(v).get_edges_tags():
                if not discovered[u]:
                    # mark it as discovered and enqueue it
                    discovered[u] = True
                    q.append(u)
    
        return False

    def get_vertix_from_tag(self, tag: str) -> Vertix:
        for vertix in self.vertices:
            if vertix.tag == tag:
                return vertix

    def get_vertices_from_tags(self, tags: list) -> List[Vertix]:
        result = []
        for vertix in self.vertices:
            is_there = len([tag for tag in tags if tag == vertix.tag]) > 0
            if is_there:
                result.append(vertix)
            
        return result

    def get_edges(self):
        result = defaultdict(list)

        for vertix in self.vertices:
            result[vertix.tag].append(vertix.edges)

        return result

    def get_vertices_tag(self) -> List[str]:
        return [vertix.tag for vertix in self.vertices]



class GraphDict:

    def __init__(self, num_vertices: int, max_edges: int) -> None:
        self.graph = np.zeros((num_vertices, num_vertices), dtype=int)
        self.max_edges = max_edges

    def create(self) -> None:
        n, _ = self.graph.shape
        counter_edges = defaultdict(lambda: 0)
        for j in range(n):
            for i in range(n):
                if self.graph[j][i] == 1 or j == i: continue
                random.seed(time.clock())
                rnd_result = random.randint(0, 1)
                if  rnd_result == 1 and counter_edges[j] < self.max_edges and counter_edges[i] < self.max_edges:
                    self.graph[j][i] = self.graph[i][j] = rnd_result
                    counter_edges[j] = counter_edges[j] + 1
                    if i != j:
                        counter_edges[i] = counter_edges[i] + 1

        return self.graph