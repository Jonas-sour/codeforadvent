def getInput(path):
    page_ordering_rules = []
    update = []

    with open(path, 'r') as file:
        lines = file.readlines()

    is_second_section = False

    for line in lines:
        line = line.strip()
        if not line:
            is_second_section = True
            continue
        if is_second_section:
            update.append([int(x) for x in line.split(',')])
        else:
            page_ordering_rules.append([int(x) for x in line.split('|')])

    return page_ordering_rules, update
def applyOrderingRules(update, page_ordering_rules):
    for order_rule in page_ordering_rules:
        try:
            index = update.index(order_rule[0])
        except:
            continue
        for i in range(index):
            if update[i] == order_rule[1]:
                return False
    return True



if __name__ == '__main__':
    page_ordering_rules, updates = getInput("pages")
    summe = 0
    for update in updates:
        if(applyOrderingRules(update, page_ordering_rules)):
            summe += update[int(len(update)/2)]
    print(summe)