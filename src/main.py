import rubik
import solver
import time
from sys import argv, stderr

def printPath(path):
    """
        Print path
        Parameters:
                path: List with moves to reach solution
    """
    if path != None:
        print("Number of moves:",len(path))
        print("Path:")
        for i in path:
            print(i, end = ' ')
        print()
    else:
        print("No solution found")

def showSolution(cube, solution, color=False):
    """
        Display animation solving cube
        Parameters:
                cube: Tuple representing scrambled cube
                solution: List of moves to solve cube
    """
    current = cube
    rubik.print3DCube(current, color)

    for i in solution:
        current = rubik.applyMove(current, i)
        time.sleep(1)
        print('\x1b[6F', end='')
        rubik.print3DCube(current, color)

def solve(cube, method='a_star'):
    """
        Solve cube using BFS or A* and print moves to reach solution.
        Parameters:
                cube: Tuple representing scrambled cube
    """
    if method == 'bfs':
        path = solver.bfs(cube, rubik.createCube())
    else:
        path = solver.a_search(cube, rubik.createCube())
    printPath(path)
    answer = input('Show solution? (Y/N) ')
    if answer == 'y' or answer == 'Y':
        showSolution(cube, path, color=True)


def init(maxScrambles=None):
    """
        Generate scrambled cube

        Returns:
                Scrambled cube
    """
    # create solved cube
    cube = rubik.createCube()
    # generate scramble
    scramble = rubik.generateRandomScramble(maxScrambles)
    print("Scramble:",scramble)
    # apply scramble
    cube = rubik.applyScramble(cube, scramble)
    return cube

if __name__ == '__main__':
    if len(argv) < 2:
        print(f'Usage: python3 {argv[0]} [method] [optional: max scrambles]', file=stderr)
        print('Available methods: bfs, a_star', file=stderr)
        exit(1)
    
    maxScrambles = None
    if len(argv) > 2:
        try:
            maxScrambles = int(argv[2])
            if maxScrambles < 0:
                print('Invalid max scrambles argument. Max scrambles should be positive', file=stderr)
                exit(2)
        except:
            print('Invalid max scrambles argument. Max scrambles should be an integer', file=stderr)
    
    cube = init(maxScrambles)
    solve(cube, argv[1])