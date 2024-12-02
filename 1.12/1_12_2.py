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


def getAppearances(number, locations2):
    appearances = 0
    for number2 in locations2:
        if number == number2:
            appearances += 1
    return appearances


def getSimilarityScore(locationsOne, locationsTwo):
    similarityScore = 0
    similarities = {
        "number": None,
    }

    for number in locationsOne:
        if similarities.keys().__contains__(number):
            similarityScore += number * similarities.get(number)
        else:
            appearances = getAppearances(number, locationsTwo)
            similarities[number] = appearances
            similarityScore += number * appearances
    print(similarityScore)


if __name__ == '__main__':
    locations1, locations2 = getInput("locations")
    getSimilarityScore(locations1, locations2)
