from itertools import product


def getInput(path):
    values = []
    equations = []
    with open(path, "r") as file:
        for line in file:
            key, vals = line.split(":")
            values.append(int(key.strip()))
            equations.append(list(map(int, vals.split())))

    return values, equations


def createOperatorMatrix(length):
    return [list(p) for p in product([0, 1, 2], repeat=length)]


def evaluateExpression(x, y, operator):
    if operator == '+':
        return x + y
    if operator == '*':
        return x * y
    if operator == '||':
        return int(str(x) + str(y))


def checkEquation(equation, permutation, operators):
    result = equation[0]
    for i in range(1, len(equation)):
        result = evaluateExpression(result, equation[i], operators[permutation[i - 1]])
    return result


def trySolvingEquation(value, equation):
    operators = ("+", "*", "||")
    permutations = 3 ** (len(equation) - 1)
    possiblePermutations = createOperatorMatrix(len(equation) - 1)
    for i in range(permutations):
        if value == checkEquation(equation, possiblePermutations[i], operators):
            return value
    return 0


if __name__ == '__main__':
    values, equations = getInput("equations")
    summe = 0
    for i in range(len(values)):
        summe += trySolvingEquation(values[i], equations[i])
    print(summe)
