with open("input/q1_input.txt", "r") as f:
    measurements = [int(line.strip()) for line in f.readlines()]


def q1_p1():
    increase_count = len([measurement for index, measurement in enumerate(measurements[1:], 1) if measurement > measurements[index-1]])
    print(increase_count)


def q1_p2():
    increase_count = len([measurement for index, measurement in enumerate(measurements[3:], 3) if sum(measurements[index-2:index+1]) > sum(measurements[index-3:index])])
    print(increase_count)
