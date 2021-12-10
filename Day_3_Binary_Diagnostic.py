def getPositionList(list_, pos):
    return [[int(bits[pos]) for bits in list_]]

def getAllPositionList(list_):
    #Take list and create a new list of list in which every list is a set of the bits in the respective position.
    pos_lists = []
    for bit in range(len(list_[0])):
        pos_lists += getPositionList(list_, bit)
    return pos_lists
    
def getCommonValue(list_):
    #Check if inside a list there are more 1's than 0's
    common = []
    for bits in list_:
        if sum(bits) >= len(bits)/2:
            common.append(1)
        else:
            common.append(0)
    return common

def getEpsilonRate(common):
    eps_rate = []
    for bit in common:
        eps_rate.append(abs(int(bit)-1))
    return eps_rate

def getConsumption(common, eps_rate):
    return convertBinaryToDecimal(common)*convertBinaryToDecimal(eps_rate)

def getOxygenRatingBits(list_):
    #Get the common value in a specific bit position and then delete every list that doesn't have the correspond bit
    remaining_ = list_[:]
    for p in range(len(list_[0])):
        if len(remaining_) == 1:
            break
        common = getCommonValue(getPositionList(remaining_, p))
        
        remaining_ = getBitsWithValue(remaining_, p, common[0])
    return remaining_[0]

def getScrubberRatingBits(list_):
    #Get the common value in a specific bit position and, invert it and then delete every list that doesn't have the correspond bit
    remaining_ = list_[:]
    for p in range(len(list_[0])):
        if len(remaining_) == 1:
            break
        common = getCommonValue(getPositionList(remaining_, p))
        uncommon = getEpsilonRate(common)

        remaining_ = getBitsWithValue(remaining_, p, uncommon[0])
    return remaining_[0]

def getBitsWithValue(list_, p, value):
    remaining_ = []
    counter = 0
    while(counter < len(list_)):
        if int(list_[counter][p]) == value:
            remaining_.append(list_[counter])
        counter += 1
    return remaining_

def convertBinaryToDecimal(binary_list):
    return int(''.join(str(bit) for bit in binary_list), 2)

with open("Day_3_file_input.txt", 'r') as file:
    bits = [list(line.rstrip()) for line in file]

common = getCommonValue(getAllPositionList(bits))
eps_rate = getEpsilonRate(common)

print(getConsumption(common, eps_rate))

oxygen_rating = getOxygenRatingBits(bits)
scrubber_rating = getScrubberRatingBits(bits)

print(getConsumption(oxygen_rating, scrubber_rating)) 
