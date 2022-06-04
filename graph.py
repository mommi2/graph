from collections import deque
from typing import List
from collections import defaultdict
from scipy.stats import gamma
import random
import time

from vertix import Vertix

class Graph:

    def __init__(self, num_vertices: int, gamma_k: int, gamma_offset: int) -> None:
        self.vertices = [Vertix(i) for i in range(num_vertices)]
        self.gamma_k = gamma_k
        self.gamma_offset = gamma_offset


    def create(self):
        num = []
        for i in range(len(self.vertices)):
            vertix = self.vertices[i]
            random.seed(time.process_time)
            rnd_value = int(gamma.rvs(self.gamma_k, loc=self.gamma_offset))
            num.append(rnd_value)
            num_edges = len(self.vertices) - 1 if rnd_value > len(self.vertices) - 1 else rnd_value
            print(f'{vertix.tag} num edges: {num_edges}')
            vertices_available = [vertix_available for vertix_available in self.vertices if vertix_available.tag != vertix.tag]
            targets = random.sample(population=vertices_available, k=num_edges)
            for target in targets:
                # vertix.add_edge(target)
                # target.add_edge(vertix)
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