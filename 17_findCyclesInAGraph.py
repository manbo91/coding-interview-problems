"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an undirected graph, determine if a cycle exists in the graph.

Here is a function signature:
"""


def find_cycle(graph):
    visited = set()

    for node in graph:
        if node in visited:
            continue

        stack = [(node, graph[node])]
        while len(stack) > 0:

            graphNode, graphNodeChildren = stack.pop()
            if graphNode in visited:
                return True

            for child in graphNodeChildren:
                if child not in stack and child not in visited:
                    stack.append((child, graphNodeChildren[child]))

            visited.add(graphNode)

    return False


graph = {'a': {'a2': {}, 'a3': {}}, 'b': {'b2': {}}, 'c': {}}

print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
