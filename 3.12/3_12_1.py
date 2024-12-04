import re
def getInput(path):
    try:
        with open(path, 'r') as file:
            corrupted_program = file.read()

    except Exception as e:
        print("something wrong")

    return corrupted_program

def findMuls(corruptedProgram):
    pattern = r"mul\((-?\d+(\.\d+)?),(-?\d+(\.\d+)?)\)"
    matches = re.findall(pattern, corruptedProgram)
    return matches

def calculateSum(matches):
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[2])
    return sum

if __name__ == '__main__':
    corrupted_program = getInput("corrupted_program")
    matches = findMuls(corrupted_program)
    summe = calculateSum(matches)
    print(summe)