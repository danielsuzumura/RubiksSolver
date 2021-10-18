import rubik
import heuristic
from Node import Node
from time import time

def path(parent, start, end):
    """
        Generate path from end to start using parent information
    """
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
    """
        Generate minimun solution for given configuration of cube
        Parameters:
                start: Cube to be solved
                end: Solved cube
    """
    queue = []
    queue.append(start)
    # store the nodes visited and the move appllied to get to node
    parent = {start: None}

    start_time = time()
    while queue:
        node = queue.pop(0)
        if node == end:
            total_time = time() - start_time
            print('BFS total time:', total_time)
            return path(parent, start, node)
        # apply every move(U,U',F,F',R,R') to current node of the cube to get the neighbors
        for move in rubik.moveName:
            temp = rubik.applyMove(node, move)
            # only add node if not visited
            if temp not in parent:
                parent[temp] = move
                queue.append(temp)
    total_time = time() - start_time
    print('BFS total time:', total_time)
    # No solution found
    return None


def calculateDistance(cube, end):
    count = 0
    for i in range(rubik.size):
        if cube[i] != end[i]:
            count += 1
    return count

def h(cube):
    dist = heuristic.get_distances()[str(cube)]
    return dist

def a_search(start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.f = 0
    start_node.h = h(start)
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = [start_node]
    closed_list = []

    start_time = time()
    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            total_time = time() - start_time
            print('BFS total time:', total_time)
            path = []
            current = current_node
            while current is not None:
                if current.previousMove != None:
                    path.append(current.previousMove)
                    current = current.parent
                else:
                    break
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for move in rubik.moveName: # Adjacent squares
            temp = rubik.applyMove(current_node.cube, move)

            # Create new node
            new_node = Node(current_node, temp, move)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            # child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            # child.h = calculateDistance(child.cube, end)
            child.h = h(child.cube)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
    total_time = time() - start_time
    print('BFS total time:', total_time)