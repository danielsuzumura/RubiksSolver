from rubik import Rubik

cube = Rubik()
scramble = cube.generateRandomScramble()
print(scramble)
cube.printCube()