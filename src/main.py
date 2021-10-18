import rubik
import solver
import time

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

def solve(cube):
    # path = solver.bfs(cube, rubik.createCube())
    # printPath(path)
    path = solver.a_search(cube, rubik.createCube())
    printPath(path)
    answer = input('Show solution? (Y/N) ')
    if answer == 'y' or answer == 'Y':
        showSolution(cube, path, color=True)


def init():
    # create solved cube
    cube = rubik.createCube()
    # generate scramble
    scramble = rubik.generateRandomScramble()
    print("Scramble:",scramble)
    # apply scramble
    cube = rubik.applyScramble(cube, scramble)
    return cube

if __name__ == '__main__':
    cube = init()
    solve(cube)