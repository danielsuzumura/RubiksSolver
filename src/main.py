import rubik
import solver

def printPath(path):
    if path != None:
        print("Number of moves:",len(path))
        print("Path:")
        for i in path:
            print(i, end = ' ')
        print()
    else:
        print("No solution found")

def solve(cube):
    # path = solver.bfs(cube, rubik.createCube())
    # printPath(path)
    path = solver.a_search(cube, rubik.createCube())
    printPath(path)

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