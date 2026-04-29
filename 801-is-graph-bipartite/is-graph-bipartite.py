class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [2] * n

        for i in range(n):
            if color[i] != 2:
                continue

            queue = deque([i])
            color[i] = 0

            while queue:
                u = queue.popleft()

                for v in graph[u]:

                    if color[v] == 2:
                        color[v] = 1 - color[u]
                        queue.append(v)

                    elif color[v] == color[u]:
                        return False

        return True

