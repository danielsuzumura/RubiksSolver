import rubik
import json

START = rubik.createCube()
distances = {}

def generate_positions():
    """
        Generate minimun solution for given configuration of cube
        Parameters:
                start: Cube to be solved
                end: Solved cube
    """
    queue = []
    queue.append((START, 0))
    # store the nodes visited and the move appllied to get to node
    global distances
    distances = {str(START): 0}

    dist = 0
    while queue and dist <= 6:
        dist += 1
        node, dist = queue.pop(0)
        # apply every move(U,U',F,F',R,R') to current node of the cube to get the neighbors
        for move in rubik.moveName:
            temp = rubik.applyMove(node, move)
            # only add node if not visited
            if str(temp) not in distances:
                distances[str(temp)] = dist+1
                queue.append((temp, dist+1))

    with open('database.json', 'w') as f:
        f.write(json.dumps(distances))

def get_distances():
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