# https://www.hackerrank.com/challenges/components-in-graph
# uses union find algorithm with weighted-quick union implementation
# see: http://algs4.cs.princeton.edu/15uf/

from sys import stdin


class UnionGraph:
    def __init__(self):
        self.num_edges = int(stdin.readline())
        self.num_nodes = 2*self.num_edges
        self.parent = [x for x in range(self.num_nodes)]
        self.component_size = [1 for _ in self.parent]

        # read in graph edges and merge components
        for _ in range(self.num_edges):
            line = stdin.readline()
            x, y = (int(num)-1 for num in line.split()) # handle off-by-1 caused by 1-indexed terms
            self.merge(x, y)

    def find_min_max_comp(self):
        # find largest and smallest connected components (sets) in the graph
        max_comp_size = 0
        min_comp_size = self.num_nodes
        for idx in range(self.num_nodes):
            # if root of component "tree"
            if self.parent[idx] == idx and self.component_size[idx] != 1:
                max_comp_size = max(max_comp_size, self.component_size[idx])
                min_comp_size = min(min_comp_size, self.component_size[idx])
        return min_comp_size, max_comp_size

    # helper function: merges two components (sets) according to union find algorithm
    def merge(self, x, y):
        x_comp_root = self.find_comp_root(x)
        y_comp_root = self.find_comp_root(y)
        # x and y are not in the same component
        if x_comp_root != y_comp_root:
            # x is in a smaller component than y
            if self.component_size[x_comp_root] < self.component_size[y_comp_root]:
                # x's comp root points to y and y's comp size is increased
                self.parent[x_comp_root] = y_comp_root
                self.component_size[y_comp_root] += self.component_size[x_comp_root]
            # y is in a smaller component than x
            else:
                # y's comp root points to x and x's comp size is increased
                self.parent[y_comp_root] = x_comp_root
                self.component_size[x_comp_root] += self.component_size[y_comp_root]

    # helper function: find highest ancestor/root of component containing node
    def find_comp_root(self, node):
        if self.parent[node] == node:
            return node
        else:
            return self.find_comp_root(self.parent[node])

my_graph = UnionGraph()
min_comp, max_comp = my_graph.find_min_max_comp()
print("{} {}".format(min_comp, max_comp))

    # test with cycles...ugh