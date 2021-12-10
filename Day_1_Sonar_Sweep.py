
def getIncrementCounter(list_):
    counter = 0
    for i in range(1, len(list_)):
        if list_[i] > list_[i-1]:
            counter += 1
    return counter

def getSumIncrementCounter(list_):
    counter = 0
    for i in range(len(list_)-3):
        if (list_[i] + list_[i+1] + list_[i+2] < list_[i+1] + list_[i+2] + list_[i+3]):
            counter += 1
    return counter

with open("Day_1_input_file.txt", 'r') as depth_file:
    depths = [int(line.rstrip()) for line in depth_file]

print(getIncrementCounter(depths))
print(getSumIncrementCounter(depths))
