def part_1():
    return

def most_common(data):
    new_bit = ""
    for digit in range(len(data[0])):
        sum = 0
        for bit in data:
            sum += int(bit[digit])
        if sum >= len(data)/2:
            new_bit += "1"
        else:
            new_bit += "0"
    return new_bit


def least_common(data):
    new_bit = ""
    for digit in range(len(data[0])):
        sum = 0
        for bit in data:
            sum += int(bit[digit])
        if sum < len(data) / 2:
            new_bit += "1"
        else:
            new_bit += "0"
    return new_bit


def oxygen_generator(data):
    for i in range(len(data[0])):
        number = most_common(data)
        yeet_list = []
        for j in range(len(data)):
            if data[j][i] != number[i]:
                yeet_list.append(data[j])
        for toyeet in yeet_list:
            data.remove(toyeet)
        if len(data) <= 1:
            break
    final = ""
    for k in data:
        final += k
    return int(final, 2)

def scrubber_generator(data):
    for i in range(len(data[0])):
        number = least_common(data)
        yeet_list = []
        for j in range(len(data)):
            if data[j][i] != number[i]:
                yeet_list.append(data[j])
        for toyeet in yeet_list:
            data.remove(toyeet)
        if len(data) <= 1:
            break
    final = ""
    for k in data:
        final += k
    return int(final, 2)



def part_2():

    return



def read_file():
    anything = []
    with open("input.txt") as file:
        for line in file:
            anything.append(line.rstrip())
    return anything


if __name__ == '__main__':
    data1 = read_file()
    data2 = read_file()
    a = scrubber_generator(data1)
    b = oxygen_generator(data2)
    print(a)
    print(b)
    print(a * b)
    # part 1
    #print(part_2())
