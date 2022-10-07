def dijkstra(graph, source, target):
    # initialize
    dist = {source: 0}
    prev = {}
    queue = set(graph.keys())
    # loop
    while queue:
        # get the node with the smallest distance
        u = min(queue, key=dist.get)
        # if the target is reached, stop
        if u == target:
            break
        # remove the node from the queue
        queue.remove(u)
        # update the distances
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if v not in dist or alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    # return the shortest path
    path = []
    u = target
    while u in prev:
        path.append(u)
        u = prev[u]
    path.append(source)
    path.reverse()
    return path