import numpy as np


def getInput(path):
    with open(path, 'r') as file:
        topoMap = [list(line.strip()) for line in file]
    return topoMap


def countEntriesInRow(trailheadMatrixRowIndex):
    ways = 0
    for j in range(len(trailheadMatrix[trailheadMatrixRowIndex])):
        if trailheadMatrix[trailheadMatrixRowIndex][j] != 0 and graph[j] == '9':
            ways += trailheadMatrix[trailheadMatrixRowIndex][j]
    return ways


def positionsValid(position, move):
    if (position + 1) % len(topoMap) == 0 and move == position+1:
        return False
    if position % len(topoMap) == 0 and position-1 == move:
        return False
    if position < len(topoMap) and (move > len(graph) - len(topoMap)):
        return False
    if position > len(graph) - len(topoMap) and move < len(topoMap):
        return False
    if abs(position - move) == 1:
        return True
    if abs(position - move) == len(topoMap):
        return True
    return False

if __name__ == '__main__':
    topoMap = getInput("topographicMap")
    graph = []
    for level in topoMap:
        for entry in level:
            graph.append(entry)
    adjazenzMatrix = np.zeros((len(topoMap) * len(topoMap[0]), len(topoMap) * len(topoMap[0])), int)
    for i in range(len(graph)):
        for j in range(len(graph)):
            if int(graph[j]) - int(graph[i]) == 1 and positionsValid(i, j):
                adjazenzMatrix[i][j] = 1
    trailheadMatrix = np.linalg.matrix_power(adjazenzMatrix, 9)
    trailheads = 0
    for i in range(len(graph)):
        if graph[i] == '0':
            trailheads += countEntriesInRow(i)
    print(trailheads)
