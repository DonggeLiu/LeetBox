class Solution(object):

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        terminal_index = len(graph) - 1
        paths = [[0]]
        ans = []

        while paths:
            path = paths.pop()

            for i in graph[path[-1]]:
                if i == terminal_index:
                    ans.append(path + [i])
                else:
                    paths.append(path + [i])
        return ans
