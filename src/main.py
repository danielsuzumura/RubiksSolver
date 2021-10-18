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

# create solved cube
cube = rubik.createCube()
# generate scramble
scramble = rubik.generateRandomScramble()
print("Scramble:",scramble)
# apply scramble
cube = rubik.applyScramble(cube, scramble)
# rubik.printCube(cube)

# path = solver.bfs(cube, rubik.createCube())
path = solver.a_search(cube, rubik.createCube())
printPath(path)
# rubik.printCube(cube)
