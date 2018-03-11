class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths = [[0]]
        valid_paths = []
        for i in range(len(graph)):
            new_path = []
            for path in paths:
                if path[-1] == (len(graph) - 1):
                    valid_paths.append(path)
                else:
                    new_path.extend([path + [node] for node in graph[path[-1] ]])
            print(i, paths, new_path)

            paths = new_path
        return valid_paths