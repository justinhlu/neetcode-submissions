"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {None:None}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]
            if node:
                newNode = Node(node.val)
                nodeMap[node] = newNode
                for nei in node.neighbors:
                    clonedNeighbor = dfs(nei)
                    newNode.neighbors.append(clonedNeighbor)
                
                return newNode

        if node:
            return dfs(node)

        return None
            