"""
Question
https://leetcode.com/problems/course-schedule-ii/
"""


class Solution:

    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Consider a graph where each course is a node pointed by an edge from its prerequisites
        edges = {i: [] for i in range(0, numCourses)}
        indegree = {}
        for dest, src in prerequisites:
            edges[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        # If the indegree of a node is zero, then that course has no untaken prerequisite
        zero_indegrees = [i for i in range(0, numCourses) if i not in indegree]
        order = []
        while zero_indegrees:
            vertex = zero_indegrees.pop(0)
            order.append(vertex)
            for dest in edges.get(vertex, []):
                indegree[dest] -= 1
                if not indegree[dest]:
                    zero_indegrees.append(dest)

        # If this does not cover all courses, then there must be a closed cycle (deadlock)
        return order if len(order) == numCourses else []

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {i: [] for i in range(0, numCourses)}
        for dest, src in prerequisites:
            edges[src].append(dest)

        order = []
        cycle = False
        colors = [0] * numCourses

        def dfs(node):
            nonlocal cycle

            if cycle:
                return []

            colors[node] = 1
            for dest in edges.get(node, []):
                if not colors[dest]:
                    dfs(dest)
                elif colors[dest] == 1:
                    cycle = True
            colors[node] = 2
            order.append(node)

        for course in range(numCourses):
            if not colors[course]:
                dfs(course)
        return [] if cycle else order[::-1]
