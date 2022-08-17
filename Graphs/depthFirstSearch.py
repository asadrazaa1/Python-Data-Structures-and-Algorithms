def DFS(g, u, discovered):
    """Perform DFS fof the undiscovered portion of Graph g starting at Vertex u

    discovered is a dictionary mapping each vertex to the edge that was to
    discover it during the DFS(u should be 'discovered' prior to the call)
    Newly discovered vertices will be added to the dictionary as a result"""
    for e in g.incident_edges(u):  # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:  # v is an unvisited vertex
            discovered[v] = e  # e is the edge that discovered v
            DFS(g, v, discovered)  # recursively explore from v
