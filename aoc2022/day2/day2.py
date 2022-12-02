
def read_file():
    anything = []
    with open("input.txt") as file:
        for line in file:
            opponent, mine = line.split(" ")
            anything.append((opponent.strip(), mine.strip()))
    return anything

def part1():
    total_sum = 0
    for i in range(len(data)):
        other = data[i][0]
        mine = data[i][1]
        shape = 0
        score = 0
        if mine == 'X':
            shape = 1
            if other == 'A':
                score = 3
            elif other == 'B':
                score = 0
            elif other == 'C':
                score = 6
        elif mine == 'Y':
            shape = 2
            if other == 'A':
                score = 6
            elif other == 'B':
                score = 3
            elif other == 'C':
                score = 0
        elif mine == 'Z':
            shape = 3
            if other == 'A':
                score = 0
            elif other == 'B':
                score = 6
            elif other == 'C':
                score = 3
        total_sum += score + shape
        print(total_sum)
    return total_sum

def part2():
    total_sum = 0
    for i in range(len(data)):
        outcome = data[i][1]
        other = data[i][0]
        if outcome == 'X' and other == 'A':
            total_sum += 3
        if outcome == 'X' and other == 'B':
            total_sum += 1
        if outcome == 'X' and other == 'C':
            total_sum += 2
        if outcome == 'Y' and other == 'A':
            total_sum += 4
        if outcome == 'Y' and other == 'B':
            total_sum += 5
        if outcome == 'Y' and other == 'C':
            total_sum += 6
        if outcome == 'Z' and other == 'A':
            total_sum += 8
        if outcome == 'Z' and other == 'B':
            total_sum += 9
        if outcome == 'Z' and other == 'C':
            total_sum += 7
    return total_sum

if __name__ == '__main__':
    data = read_file()
    # print(data)
    # part 1
    print(part2())
