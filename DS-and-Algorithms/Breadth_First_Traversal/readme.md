Write Program for Breadth First Traversal in Python, C++, Java, and JavaScript

## Logic

```
BreadthFirstTraversal(graph, root):
  create empty queue and push root node to it
  create empty set to store visited nodes
  while queue is not empty
    pop node from queue and mark it as visited
    for each node in graph.adjacentNodes(node)
      if node is not visited
        push node to queue
end BreadthFirstTraversal
```
