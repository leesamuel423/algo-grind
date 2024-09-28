from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Adjacency List and Edges List
        adj = defaultdict(list)
        edges = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            edges[course] += 1

        # Queue of courses with no prereqs -> BFS
        zero_edges = deque([i for i in range(numCourses) if edges[i] == 0])
        final = []

        while zero_edges:
            course = zero_edges.popleft()
            final.append(course)

            for neighbor in adj[course]:
                edges[neighbor] -= 1
                if edges[neighbor] == 0:
                    zero_edges.append(neighbor)

        return final if len(final) == numCourses else []
