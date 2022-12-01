def part_1():
    hor = 0
    vert = 0
    for dir, dis in data:
        if dir == 'forward':
            hor += dis
        elif dir == 'down':
            vert += dis
        else:
            vert -= dis
    return hor * vert


def part_2():
    hor = 0
    aim = 0
    vert = 0
    for dir, dis in data:
        if dir == "forward":
            hor += dis
            vert += aim * dis
        elif dir == "down":
            aim += dis
        else:
            aim -= dis
    return hor * vert



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
