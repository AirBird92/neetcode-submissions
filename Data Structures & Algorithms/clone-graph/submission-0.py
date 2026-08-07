"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, nodeMap):
            if node in nodeMap:
                return nodeMap[node]
            
            clone = Node(node.val)
            nodeMap[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor, nodeMap))
            return clone
        return dfs(node, {}) if node else None