
def getInput(path):
    try:
        with open(path, 'r') as file:
            rows = file.readlines()

    except Exception as e:
        print("something wrong")

    seperateRows = []

    for row in rows:
        intArray = list(map(int, row.strip().split()))
        seperateRows.append(intArray)

    return seperateRows

def isReportSafe(report_in_function):
    if len(report_in_function) == 1:
        return 0
    if report_in_function[0] > report_in_function[1]:
        report_in_function.reverse()
    for i in range(len(report_in_function)-1):
        if report_in_function[i+1] - report_in_function[i] > 3 or report_in_function[i+1] - report_in_function[i] <= 0:
            return 0
    return 1

if __name__ == '__main__':
    reports = getInput("reports")
    saves = 0
    for report in reports:
        saves += isReportSafe(report)
    print(saves)
