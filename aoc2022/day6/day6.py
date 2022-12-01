def little_fuel(data):
    total_list = []
    for i in range(max(data)):
        sum = 0
        for j in data:
            sum += summer(abs(j - i))
        total_list.append(sum)
    lowest = min(total_list)
    return lowest


def summer(step):
    return (len(step) * (len(step) + 1))/2



def read_file():
    anything = []
    with open("input.txt") as file:
        for line in file:
            anything.append(line.rstrip())
    g = anything[0].split(',')
    h = []
    for j in g:
        h.append(int(j))
    return h

if __name__ == '__main__':
        data = read_file()
        print(little_fuel(data))
        print(summer(3))
