import re
def getInput(path):
    try:
        with open(path, 'r') as file:
            corrupted_program = file.read()

    except Exception as e:
        print("something wrong")

    return corrupted_program

    matches = re.findall(pattern, corruptedProgram)
def findMuls(corruptedProgram):
    pattern = r"mul\((-?\d+(\.\d+)?),(-?\d+(\.\d+)?)\)"
    matches = re.findall(pattern, corruptedProgram)
    return matches

def calculateSum(matches):
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[2])
    return sum
def findNextDont(corruptedProgram):
    pattern = r"\bdon't\b"
    firstSubstring = re.split(pattern, corruptedProgram, 1)
    return firstSubstring

def fromDontToDo(corruptedProgram):
    pattern = r"\bdo\b"
    firstSubstring = re.split(pattern, corruptedProgram, 1)
    return firstSubstring
if __name__ == '__main__':
    cleanedProgram = []
    corrupted_program = getInput("corrupted_program")
    programToFirstDont = findNextDont(corrupted_program)
    cleanedProgram.append(programToFirstDont[0])
    restProgram = programToFirstDont[1]
    exception = 0
    while(exception == 0):
        try:
            restProgram = fromDontToDo(restProgram)
            programToFirstDont = findNextDont(restProgram[1])
            cleanedProgram.append(programToFirstDont[0])
            restProgram = programToFirstDont[1]
        except:
            exception = 1
    programString = "".join(cleanedProgram)
    matches = findMuls(programString)
    summe = calculateSum(matches)
    print(summe)