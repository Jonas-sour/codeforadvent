def getInput(path):
    with open(path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def positionAufKarte(position):
    if 0 <= position[0] < len(karte) and 0 <= position[1] < len(karte):
        return True


def updateAntennas(antenna, antennaLocation):
    if antennas.keys().__contains__(antenna):
        antennas[antenna].append(antennaLocation)
    else:
        antennas[antenna] = [antennaLocation]


def buildDirectionary(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                updateAntennas(grid[i][j], (i, j))
    return antennas


def calculateAntinodes(antennaLocations):
    for j in range(len(antennaLocations)):
        for i in range(len(antennaLocations)):
            if j != i:
                distanceModifier = 1
                onKarte = True
                while onKarte:
                    antinode = (antennaLocations[j][0] - ((antennaLocations[j][0] - antennaLocations[i][0]) * distanceModifier),
                                antennaLocations[j][1] - ((antennaLocations[j][1] - antennaLocations[i][1]) * distanceModifier))
                    if positionAufKarte(antinode):
                        if not antinodes.__contains__(antinode):
                            antinodes.append(antinode)
                    else:
                        onKarte=False
                    distanceModifier += 1


if __name__ == '__main__':
    karte = getInput("antennas")
    antinodes = []
    antennas = {}
    buildDirectionary(karte)
    for key in antennas.keys():
        calculateAntinodes(antennas[key])
    print(len(antinodes))
