def part1():
    twos = 0
    threes = 0
    letterlist = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            letterlist.add(data[i][j])
    for i in range(len(data)):
        specific_twos = 0
        specific_threes = 0
        for k in letterlist:
            lettersum = 0
            for j in range(len(data[0])):
                if data[i][j] == k:
                    lettersum += 1
            if lettersum == 2:
                specific_twos += 1
            if lettersum == 3:
                specific_threes += 1
        if specific_twos >= 1:
            twos += 1
        if specific_threes >= 1:
            threes += 1
    return twos*threes

def part2():
    for i in range(len(data)):
        for j in range(len(data)):
            letter_differ = 0
            if j != i:
                for k in range(len(data[0])):
                    if data[i][k] != data[j][k]:
                        letter_differ += 1
            if letter_differ == 1:
                return data[i], data[j], data[i][k], i, j

def read_file():
    anything = []
    with open("input") as file:
        for line in file:
            anything.append(line.rstrip())
    return anything

if __name__ == '__main__':
    data = read_file()

    # part 1
    print(part2())
