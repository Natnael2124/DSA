class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course, preq in prerequisites:
            graph[preq].append(course)

        color = [0] * numCourses
        res = []

        def dfs(node):
            if color[node] == 1:
                return False
            
            if color[node] == 2:
                return True
            
            color[node] = 1
            
            for i in graph[node]:
                if not dfs(i):
                    return False

            color[node] = 2
            res.append(node)
            return True

        for j in range(numCourses):
            if color[j] == 0:
                if not dfs(j):
                    return []

        return res[::-1]

            

