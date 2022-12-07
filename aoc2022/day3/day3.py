def retrieve_letters():
    total_list = []
    for i in range(len(data)):
        first = data[i][0:len(data[i])//2]
        second = data[i][len(data[i])//2:]
        for j in range(len(second)):
            if second[j] in first:
                total_list.append(second[j])
                break
    return total_list

def group_badge():
    total_list = []
    i = 0
    while i < len(data):
        j = i + 1
        k = i + 2
        for a in data[i]:
            if a in data[j] and a in data[k]:
                total_list.append(a)
                break
        i += 3
    return total_list

def put_value(l_list):
    total_sum = 0
    for i in l_list:
        addi = 0
        if ord(i) - ord('a') >= 0:
            addi = ord(i) - ord('a') + 1
        else:
            addi = ord(i) - ord('A') + 27
        print(addi)
        total_sum += addi
    return total_sum

def read_file():
    anything = []
    with open("input.txt") as file:
        for line in file:
            anything.append(line.rstrip())
    return anything


if __name__ == '__main__':
    data = read_file()
    print(group_badge())
    print(put_value(group_badge()))
    #print(part_2())
