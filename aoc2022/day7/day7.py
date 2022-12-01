

def part_2():

    return



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
        print(data)
