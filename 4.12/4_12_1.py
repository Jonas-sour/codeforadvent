def getInput(path):
    try:
        with open(path, 'r') as file:
            rows = file.read().splitlines()

    except Exception as e:
        print("something wrong")

    return rows


def searchXMASright(ceres, row, column):
    if column + 3 < len(ceres[0]):
        if ceres[row][column + 1] == 'M' and ceres[row][column + 2] == 'A' and ceres[row][column + 3] == 'S':
            return 1
    return 0


def searchXMASleft(ceres, row, column):
    if column - 3 >= 0:
        if ceres[row][column - 1] == 'M' and ceres[row][column - 2] == 'A' and ceres[row][column - 3] == 'S':
            return 1
    return 0


def searchXMASup(ceres, row, column):
    if row - 3 >= 0:
        if ceres[row - 1][column] == 'M' and ceres[row - 2][column] == 'A' and ceres[row - 3][column] == 'S':
            return 1
    return 0


def searchXMASdown(ceres, row, column):
    if row + 3 < len(ceres):
        if ceres[row + 1][column] == 'M' and ceres[row + 2][column] == 'A' and ceres[row + 3][column] == 'S':
            return 1
    return 0


def searchXMASdiagleftdown(ceres, row, column):
    if column - 3 >= 0 and row + 3 < len(ceres):
        if ceres[row + 1][column - 1] == 'M' and ceres[row + 2][column - 2] == 'A' and ceres[row + 3][
            column - 3] == 'S':
            return 1
    return 0


def searchXMASdiagleftup(ceres, row, column):
    if column - 3 >= 0 and row - 3 >= 0:
        if ceres[row - 1][column - 1] == 'M' and ceres[row - 2][column - 2] == 'A' and ceres[row - 3][
            column - 3] == 'S':
            return 1
    return 0


def searchXMASdiagrightdown(ceres, row, column):
    if row + 3 < len(ceres) and column + 3 < len(ceres[0]):
        if ceres[row + 1][column + 1] == 'M' and ceres[row + 2][column + 2] == 'A' and ceres[row + 3][
            column + 3] == 'S':
            return 1
    return 0


def searchXMASdiagrightup(ceres, row, column):
    if column + 3 < len(ceres[0]) and row - 3 >= 0:
        if ceres[row - 1][column + 1] == 'M' and ceres[row - 2][column + 2] == 'A' and ceres[row - 3][
            column + 3] == 'S':
            return 1
    return 0


if __name__ == '__main__':
    ceres = getInput("ceres_search")
    summe = 0
    for i in range(len(ceres)):
        for j in range(len(ceres[0])):
            if (ceres[i][j]) == 'X':
                summe += searchXMASright(ceres, i, j)
                summe += searchXMASleft(ceres, i, j)
                summe += searchXMASup(ceres, i, j)
                summe += searchXMASdown(ceres, i, j)
                summe += searchXMASdiagrightup(ceres, i, j)
                summe += searchXMASdiagleftup(ceres, i, j)
                summe += searchXMASdiagrightdown(ceres, i, j)
                summe += searchXMASdiagleftdown(ceres, i, j)
    print(summe)
