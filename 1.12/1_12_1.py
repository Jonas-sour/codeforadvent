import numpy as np
def getInput(path):
    locations1 = []
    locations2 = []

    try:
        with open(path, 'r') as file:
            for line in file:
                num1, num2 = map(int, line.split())
                locations1.append(num1)
                locations2.append(num2)
    except Exception as e:
        print("something wrong")

    return locations1, locations2


def getDistance(locations1, locations2):
    sortedLocations1 = sorted(locations1)
    sortedLocations2 = sorted(locations2)

    distance = sum(abs(np.array(sortedLocations1)-np.array(sortedLocations2)))
    print(distance)

if __name__ == '__main__':
    locations1, locations2 = getInput("locations")
    getDistance(locations1, locations2)