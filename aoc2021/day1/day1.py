import numpy as np
import pandas as pd


def read_file():
    with open("input.txt") as file:
        return [int(x) for x in file]


if __name__ == '__main__':
    data = read_file()
    sum = 0
    for i in range(len(data)):
        if i < len(data)-3:
            if (data[i] + data[i+1] + data[i+2]) < (data[i+1] + data[i+2] + data[i+3]):
                sum += 1
    print(sum)

