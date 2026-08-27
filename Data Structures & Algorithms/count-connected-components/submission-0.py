class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        def dfs(node, parent):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i, -1)
        return res