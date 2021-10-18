import rubik
import solver
import time
import re
from sys import argv, stderr

def printPath(path):
    if path != None:
        print("Number of moves:",len(path))
        print("Path:")
        for i in path:
            print(i, end = ' ')
        print()
    else:
        print("No solution found")

def showSolution(cube, solution, color=False):
    current = cube
    rubik.print3DCube(current, color)
    
    for i in solution:
        current = rubik.applyMove(current, i)
        time.sleep(1)
        print('\x1b[6F', end='')
        rubik.print3DCube(current, color)

def solve(cube, method='a_star'):
    if method == 'bfs':
        path = solver.bfs(cube, rubik.createCube())
    else:
        path = solver.a_search(cube, rubik.createCube())
    printPath(path)

    answer = input('Show solution? (Y/N) ')
    if answer == 'y' or answer == 'Y':
        showSolution(cube, path, color=True)


def init(maxScrambles=None, scrambles=None):
    # create solved cube
    cube = rubik.createCube()
    # generate scramble
    scramble = rubik.generateRandomScramble(maxScrambles) if scrambles is None else scrambles
    print("Scramble:",scramble)
    # apply scramble
    cube = rubik.applyScramble(cube, scramble)
    return cube

if __name__ == '__main__':
    # Check if the arguments were passed
    if len(argv) < 2:
        print(f'Usage: python3 {argv[0]} [method] [optional: max scrambles or scramble]', file=stderr)
        print('Available methods: bfs, a_star', file=stderr)
        exit(1)
    
    # Parse arguments
    maxScrambles = None
    scrambles = None
    if len(argv) > 2:
        try:
            # Try to parse an max scrambles argument
            maxScrambles = int(argv[2])
            #check if it's valid
            if maxScrambles < 0:
                print('Invalid max scrambles argument. Max scrambles should be positive', file=stderr)
                exit(2)
        except:
            # Try to parse an scrambles argument
            scrambles = str(argv[2])
            # Check if it's valid
            if len(''.join(re.split('\[|F|R|U|i|\'|,|\]| ', scrambles))) > 0:
                print('Invalid scrambles argument', file=stderr)
                exit(3)
            # Build list of scrambles
            scrambles = list(filter(None, re.split('[\[,\'\] ]', scrambles)))
    
    # Start
    cube = init(maxScrambles, scrambles)
    solve(cube, argv[1])