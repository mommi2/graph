from typing import List

class Vertix(object):

    def __init__(self, tag, edges: list = None) -> None:
        self.tag = tag
        self.edges = edges or []

    def add_edge(self, target) -> None:
        if target in self.edges:
            return
        self.edges.append(target)

    def get_edges_tags(self) -> List[str]:
        return [edge.tag for edge in self.edges]