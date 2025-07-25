class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Dictionary to map original node -> cloned node
        cloned = {}

        def dfs(current):
            # If already cloned, return it
            if current in cloned:
                return cloned[current]

            # Clone the current node
            copy = Node(current.val)
            cloned[current] = copy

            # Clone all neighbors
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
