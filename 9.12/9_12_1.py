def getInput(path):
    try:
        with open(path, 'r') as file:
            file = file.read()

    except Exception as e:
        print("something wrong")

    return file


def ergaenzeSortedDiskFile(index, amount):
    for i in range(int(amount)):
        sortedDisk.append(index)


def ergaenzeSortedSidkFreeSpace(amount):
    for i in range(int(amount)):
        sortedDisk.append('.')


def sortDisk():
    index = 0
    for i in range(len(disk)):
        if i % 2 == 0:
            ergaenzeSortedDiskFile(index, disk[i])
            index += 1
        else:
            ergaenzeSortedSidkFreeSpace(disk[i])


def findIndexNext(j):
    while sortedDisk[j] == '.':
        j -= 1
    return j


def defragmentDisk():
    j = len(sortedDisk) - 1
    j = findIndexNext(j)
    for i in range(len(sortedDisk)):
        if sortedDisk[i] == '.' and i < j:
            tmp = sortedDisk[j]
            sortedDisk[j] = sortedDisk[i]
            sortedDisk[i] = tmp
            j = findIndexNext(j)
    return sortedDisk


if __name__ == '__main__':
    disk = getInput("disk")
    sortedDisk = []
    sortDisk()
    defragmentDisk()
    checksum = 0
    i = 0
    while i < len(sortedDisk) and sortedDisk[i] != '.':
        checksum += i * int(sortedDisk[i])
        i += 1
    print(sortedDisk)
    print(checksum)
