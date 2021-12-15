import statistics

def getPositionList(input_file):
    with open(input_file, 'r') as file:
        pos_str = file.readline()

    pos_list_str = pos_str.split(',')
    
    return [int(pos) for pos in pos_list_str]

def getFuel(steps):
    return (steps*(steps+1))/2

def getAllFuels(position_list):
    extremes = (min(position_list), max(position_list))

    lowest_fuel_sum = float('inf')
    for i in range(extremes[0], extremes[1]+1):
        current_fuel_sum = 0
        for p in position_list:
            current_fuel_sum += getFuel(abs(p-i))
        if current_fuel_sum < lowest_fuel_sum:
            lowest_fuel_sum = current_fuel_sum
    return lowest_fuel_sum

def main(position_list):
    print(getAllFuels(position_list))
    return None


if __name__ == '__main__':
    input_file = "Day_7_input_file.txt"
    #Day_7_input_file.txt
    position_list = getPositionList(input_file)
    main(position_list)
