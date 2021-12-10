def getHorizontalPosition(list_):
    pos = 0
    for i in list_:
        if i[0] == "forward":
            pos += int(i[1])
    return pos

def getDepth(list_):
    depth = 0;
    for i in list_:
        if i[0] == "up":
            depth -= int(i[1])
        elif i[0] == "down":
            depth += int(i[1])
    return depth

def getPosition(list_):
    pos = 0
    depth = 0
    aim = 0
    for i in list_:
        v = int(i[1])
        if i[0] == "forward":
            pos += v
            depth += aim*v
        elif i[0] == "up":
            aim -= v
        elif i[0] == "down":
            aim += v
    return pos, depth

with open("Day_2_input_file.txt", 'r') as depth_file:
    instructions = [line.split() for line in depth_file]

print(getHorizontalPosition(instructions))
print(getDepth(instructions))
print(getPosition(instructions))
