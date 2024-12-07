def getInput(path):
    with open(path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def findStartPosition(karte):
    for i in range(len(karte)):
        for j in range(len(karte[0])):
            if karte[i][j] == '^':
                return i, j

def positionAufKarte(position, karte):
    if 0 <= position[0] < len(karte) and 0 <= position[1] < len(karte):
        return True
if __name__ == '__main__':
    karte = getInput("map")
    up = (-1, 0)
    right = (0, 1)
    left = (0, -1)
    down = (1, 0)
    directions = [up, right, down, left]
    position = findStartPosition(karte)
    karte[int(position[0])][int(position[1])] = 'X'
    visits = 1
    direction = 0
    while True:
        nextPosition = tuple(a + b for a,b in zip(position,directions[direction]))
        if not positionAufKarte(nextPosition, karte):
            break
        if karte[int(nextPosition[0])][int(nextPosition[1])] == '#':
            direction = (direction + 1) % 4
        else:
            position = nextPosition
            if karte[int(position[0])][int(position[1])] != 'X':
                karte[position[0]][position[1]] = 'X'