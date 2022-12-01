def read_file():
    with open("input.txt") as file:
        return [x.strip() for x in file]


def part1():
    max_sum = 0
    temp_sum = 0
    for i in range(len(data)):
        if data[i] == "":
            if temp_sum > max_sum:
                max_sum = temp_sum
            temp_sum = 0
        else:
            temp_sum += int(data[i])
    return max_sum


def part2():
    three_list = [0,0,0]
    temp_sum = 0
    for i in range(len(data)):
        if data[i] == "":
            if temp_sum > min(three_list):
                three_list[three_list.index(min(three_list))] = temp_sum
            temp_sum = 0
        else:
            temp_sum += int(data[i])
    if temp_sum > min(three_list):
        three_list[three_list.index(min(three_list))] = temp_sum
    return sum(three_list)

def part2_differently():
    sum_list = []
    temp_sum = 0
    for i in range(len(data)):
        if data[i] == "":
            sum_list.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(data[i])
    sum_list.append(temp_sum)
    max_sum = 0
    for i in range(3):
        max_sum += max(sum_list)
        sum_list.remove(max(sum_list))
    return max_sum



if __name__ == '__main__':
    data = read_file()
    print(part2())
    print(part2_differently())

