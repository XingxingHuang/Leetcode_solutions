# https://leetcode.com/problems/all-paths-from-source-to-target/description/


class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        iterative, since we know the maximum possible number of steps
        """
        paths = [[0]]
        valid_paths = []
        for i in range(len(graph)):
            new_path = []
            for path in paths:
                if path[-1] == (len(graph) - 1):
                    valid_paths.append(path)
                else:
                    new_path.extend([path + [node] for node in graph[path[-1]]])
            # print(i, paths, new_path)

            paths = new_path
        return valid_paths