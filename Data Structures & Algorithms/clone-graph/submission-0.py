"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]
            
            if node:
                newNode = Node(node.val)
                cloneMap[node] = newNode
                for nei in node.neighbors:
                    newNode.neighbors.append(dfs(nei))
                return newNode

        if node:
            return dfs(node)
        else:
            return None