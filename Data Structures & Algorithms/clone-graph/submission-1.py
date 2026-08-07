"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        nodeMap = {}
        nodeMap[node] = Node(node.val)

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in nodeMap:
                    nodeMap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                nodeMap[cur].neighbors.append(nodeMap[neighbor])
        return nodeMap[node]