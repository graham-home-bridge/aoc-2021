with open("input/q2_input.txt", "r") as f:
    instructions = [line.strip() for line in f.readlines()]


def q2_p1():
    x = 0
    y = 0
    for line in instructions:
        direction, distance = line.split(" ")
        if direction == "forward":
            x += int(distance)
        elif direction == "up":
            y -= int(distance)
        elif direction == "down":
            y += int(distance)
    print(x*y)


def q2_p2():
    aim = 0
    x = 0
    y = 0
    for line in instructions:
        direction, distance = line.split(" ")
        if direction == "forward":
            x += int(distance)
            y += aim * int(distance)
        elif direction == "up":
            aim -= int(distance)
        elif direction == "down":
            aim += int(distance)
    print(x*y)
