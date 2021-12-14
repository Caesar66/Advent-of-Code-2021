import time

def getFishList(input_file):
    with open(input_file, 'r') as file:
        fish_str = file.readline()

    fish_list_str = fish_str.split(',')
    
    return [int(fish) for fish in fish_list_str]

def inputCycle(fish_list):
    fish_cycles = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for fish in fish_list:
        fish_cycles[fish] += 1
    return fish_cycles

def incrementCycle(fish_cycles):
    new_fishes = fish_cycles[0]
    recycled_fishes = fish_cycles[0]
    fish_cycles[0] = 0
    
    for i in range(1, 9):
        fish_cycles[i-1] = fish_cycles[i]
        fish_cycles[i] = 0
    fish_cycles[8] = new_fishes
    fish_cycles[6] += recycled_fishes
    return fish_cycles

def countFishes(fish_cycles):
    return sum(list(fish_cycles.values()))

def main(fish_list, days_cycle):
    days = 0
    fish_cycles = inputCycle(fish_list)

    while days < days_cycle:
        fish_cycles = incrementCycle(fish_cycles)
        days += 1

    print(countFishes(fish_cycles))
    return None

if __name__ == '__main__':
    input_file = "Day_6_input_file.txt"
    fish_list = getFishList(input_file)

    main(fish_list, 256)

