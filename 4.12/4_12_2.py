def getInput(path):
    try:
        with open(path, 'r') as file:
            rows = file.read().splitlines()

    except Exception as e:
        print("something wrong")

    return rows


def searchXMAScross(ceres, row, column):
    if (column - 1 >= 0) and (column + 1 < len(ceres[0])) and (row - 1 >= 0) and (row + 1 < len(ceres)):
        if ceres[row-1][column-1] == 'M' and ceres[row+1][column+1] == 'S' and ceres[row-1][column+1] == "M" and ceres[row+1][column-1] == 'S':
            return 1
        if ceres[row-1][column-1] == 'S' and ceres[row+1][column+1] == 'M' and ceres[row-1][column+1] == "M" and ceres[row+1][column-1] == 'S':
            return 1
        if ceres[row-1][column-1] == 'M' and ceres[row+1][column+1] == 'S' and ceres[row-1][column+1] == "S" and ceres[row+1][column-1] == 'M':
            return 1
        if ceres[row-1][column-1] == 'S' and ceres[row+1][column+1] == 'M' and ceres[row-1][column+1] == "S" and ceres[row+1][column-1] == 'M':
            return 1
    return 0

if __name__ == '__main__':
    ceres = getInput("ceres_search")
    summe = 0
    for i in range(len(ceres)):
        for j in range(len(ceres[0])):
            if (ceres[i][j]) == 'A':
                summe += searchXMAScross(ceres, i, j)
    print(summe)
