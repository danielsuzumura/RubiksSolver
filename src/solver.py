import rubik

def path(parent, start, end):
    path = []
    # last node
    node = end
    # last move
    current = parent[node]
    # backtrack ancestors to get path
    while parent[node] != None:
        path.append(current)
        # reverse move to get previous node
        node = rubik.applyMove(node,rubik.inverseMove(current))
        current = parent[node]
    path.reverse()
    return path

def bfs(start, end):
    queue = []
    queue.append(start)
    # store the nodes visited and the move appllied to get to node
    parent = {start: None}

    while queue:
        node = queue.pop(0)
        if node == end:
            return path(parent, start, node)
        # apply every move(U,U',F,F',R,R') to current node of the cube to get the neighbors
        for move in rubik.moveName:
            temp = rubik.applyMove(node, move)
            # only add node if not visited
            if temp not in parent:
                parent[temp] = move
                queue.append(temp)
    # No solution found
    return None
