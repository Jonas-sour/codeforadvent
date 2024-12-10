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


def findIndexNextAndFilesize(j):
    while sortedDisk[j] == '.':
        j -= 1
    filesize = 0
    checkchar = sortedDisk[j]
    while sortedDisk[j] != '.' and sortedDisk[j] == checkchar:
        filesize += 1
        j -= 1
    return filesize, j + 1


def checkFreeSpace(index):
    freeSpace = 0
    while index < len(sortedDisk) and sortedDisk[index] == '.':
        freeSpace += 1
        index += 1
    return freeSpace


def checkForFreeSpace(size, j):
    for i in range(j):
        if sortedDisk[i] == '.':
            freeSpace = checkFreeSpace(i)
            if freeSpace >= size:
                return i
    return -1


def swapFile(freeSpaceIndex, size, fileIndex):
    for z in range(size):
        tmp = sortedDisk[fileIndex]
        sortedDisk[fileIndex] = sortedDisk[freeSpaceIndex]
        sortedDisk[freeSpaceIndex] = tmp
        freeSpaceIndex += 1
        fileIndex += 1


def defragmentDisk():
    j = len(sortedDisk) - 1
    freeSpaceIndex = 0
    while j > freeSpaceIndex:
        size, j = findIndexNextAndFilesize(j)
        freeSpaceIndex = checkForFreeSpace(size, j)
        if freeSpaceIndex == -1:
            j -= 1
            continue
        swapFile(freeSpaceIndex, size, j)


if __name__ == '__main__':
    disk = getInput("disk")
    sortedDisk = []
    sortDisk()
    defragmentDisk()
    checksum = 0
    i = 0
    while i < len(sortedDisk):
        if sortedDisk[i] == '.':
            i += 1
            continue
        checksum += i * int(sortedDisk[i])
        i += 1
    print(sortedDisk)
    print(checksum)
