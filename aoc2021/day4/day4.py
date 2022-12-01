def read_file():
    anything = []
    with open("input.txt") as file:
        for line in file:
            anything.append(line.rstrip())
    return anything



if __name__ == '__main__':
    import numpy as np
    data = read_file()
    bingo_numbers = data[0]
    non_value_list = []
    for i in range(len(data)):
        if data[i] == "":
            non_value_list.append(i)
    for i in range()
    print(non_value_list)
    # part 1
    #print(part_2())
