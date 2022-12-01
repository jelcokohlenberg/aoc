def part_1():



def part_2():



def read_file():
    anything = []
    with open("input.txt") as file:
        for line in file:
            direction, distance = line.split(" ")
            anything.append((direction, int(distance)))
    return anything


if __name__ == '__main__':
    data = read_file()
    # print(data)
    # part 1
    print(part_2())
