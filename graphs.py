import collections

class graphNode(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = None

class graphSolutions():

    def graphDistance(self, node):
        '''
        get distance of all nodes to the input node
        '''

        distance = {node: 0}
        queue = collections.deque([node])

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbers:
                if neighbor in distance:
                    continue
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

        return distance
    
    def cloneGraph(self, node):
        def cloneNodes(node):
            nodeMap = {node: graphNode(node.val)}
            queue = collections.deque([node])

            while queue:
                node = queue.popleft()
                for neighbor in node.neighbors:
                    if neighbor in nodeMap:
                        continue
                    nodeMap[neighbor] = graphNode(neighbor.val)
                    queue.append(neighbor)
            return nodeMap
        
        def cloneEdges(nodeMap):
            for node, newNode in nodeMap.items():
                newNode.neighbors = [nodeMap[n] for n in node.neighbors]

        nodeMap = cloneNodes(node)
        cloneEdges(nodeMap)

        return nodeMap[node]

        





