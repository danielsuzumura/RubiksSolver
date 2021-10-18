"""
    Generating heuristic table for A* algorithm using Patter Database.
    Based on https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf
"""

import rubik
import json
from time import time

START = rubik.createCube()
distances = {}

def generate_positions():
    """
        Generate json file with every possible combination and gives distance from
        combination to solved
    """
    queue = []
    queue.append((START, 0))
    # store the distance from solved to every possible combination
    global distances
    distances = {str(START): 0}

    start_time = time()
    # using BFS to calculate distance to every combination
    while queue:
        node, dist = queue.pop(0)
        # apply every move(U,U',F,F',R,R') to current node of the cube to get the neighbors
        for move in rubik.moveName:
            temp = rubik.applyMove(node, move)
            # only add node if not visited
            if str(temp) not in distances:
                distances[str(temp)] = dist+1
                queue.append((temp, dist+1))
    total_time = time() - start_time
    print('Heuristic generation time:', total_time)

    # store table in database.json file
    with open('database.json', 'w') as f:
        f.write(json.dumps(distances))

def get_distances():
    """
        Use database.json file to get distance
        from current combination to solved state
    """
    global distances
    if distances == {}:
        try:
            with open('database.json', 'r') as f:
                distances = json.loads(f.read())
        except:
            generate_positions()
    return distances

if __name__ == '__main__':
    generate_positions()