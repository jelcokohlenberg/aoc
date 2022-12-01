def part_1():
    total = 0
    inbetweeners = set()
    while total not in inbetweeners:
        for i in range(len(data)):
            inbetweeners.add(total)
            total += data[i]
            if total in inbetweeners:
                return total, len(inbetweeners)



def read_file():
    with open("input") as file:
        return [int(x) for x in file]


if __name__ == '__main__':
    data = read_file()

    # part 1
    print(data)

