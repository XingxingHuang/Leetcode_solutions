# https://leetcode.com/problems/is-graph-bipartite/description/
import timeit
from collections import defaultdict

class Solution:
    def isBipartite(self, graph):
        color = defaultdict(lambda: -1)
        return all(self.dfs(graph, v, edges, 0, color) for v, edges in enumerate(graph) if color[v] == -1)

    def dfs(self, graph, v, edges, cur_color, color):
        if color[v] != -1: return color[v] == cur_color
        color[v] = cur_color
        return all(self.dfs(graph, e, graph[e], int(not cur_color), color) for e in edges)

def run():
    Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
