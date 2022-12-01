def part_1():
    for i in data:
        for j in data:
            if i != j and i + j == 2020:
                return i * j


def read_file():
    with open("input.txt") as file:
        return [int(x) for x in file]


if __name__ == '__main__':
    data = read_file()

    # part 1
    print(part_1())
