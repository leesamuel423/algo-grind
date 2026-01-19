from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visited = set()
        required = [0] * numCourses

        # create adj list
        for prereq in prerequisites:
            adj_list[prereq[1]].append(prereq[0])
            required[prereq[0]] += 1
        
        # main operation
        for idx, num in enumerate(required):
            if num == 0 and idx not in visited:
                visited.add(idx)
                self.dfs(idx, required, adj_list, visited)
        
        return len(visited) == numCourses


    def dfs(self, idx, required, adj_list, visited):
        for i in adj_list[idx]:
            required[i] -= 1
            if required[i] == 0:
                visited.add(i)
                self.dfs(i, required, adj_list, visited)



"""
adjacency list
{
    requirement: [course],
    0: [1]
}

required = [0] * length
// [0, 1] -> create this while adjacency list
visited set

iterate through required, and if 0 and not in visited, dfs
    make sure you add to visisted set

return length(set) == numCourses

helper fn dfs (idx, required, adjacency list, visited)
    iterate through adjacency list[idx]
        decrement from required
        if required[whatever im decrementing] == 0
            add to visited set
            dfs ()
"""
        
