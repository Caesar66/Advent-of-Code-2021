def getAdjs(pos, line_size, list_size):
    #UP, RIGHT, DOWN, LEFT
    adjs = []
    #Check for invalid adjacents
    if(pos-line_size >= 0):
        adjs.append(pos-line_size)
        
    if(pos%line_size != line_size-1):
        adjs.append(pos+1)
        
    if(pos+line_size <= list_size-1):
        adjs.append(pos+line_size)
        
    if(pos%line_size != 0):
        adjs.append(pos-1)
        
    return adjs

def isMinimum(pos, adjs, list_):
    for p in adjs:
        if(list_[p] <= list_[pos]):
            return False
    return True

def getNextInQueue(queue_, pos_list):
    if len(queue_) > 0:
        return queue_[0]
    return -1

def getNextInPos(pos_list):
    for p in range(len(pos_list)):
        if pos_list[p] == 0:
            return p
    return -1

def cutAdjs(adjs, pos_list):
    for p in adjs:
        pos_list[p] = -1
    return pos_list

def findLows():
    queue = []
    lows = {}
    
    number_list , size_line = getPosList()

    size_list = len(number_list)
    
    #[0 : available | 1 : in queue | -1 : unavailable]
    pos_list = [0]*size_list

    while(getNextInQueue(queue, pos_list) >= 0 or getNextInPos(pos_list) >= 0):

        next_ = getNextInQueue(queue, pos_list)

        #If queue is empty, get next value on the availables list and set that one as in queue
        if(next_ < 0):
            next_ = getNextInPos(pos_list)
            queue.append(next_)
            pos_list[next_] = 1

        #If queue is not empty, check if this value is already cut, if it is, get next value
        if(pos_list[next_] == -1):
            queue = queue[1:]
            continue

        #If the value is lowest in comparison to adjacents, add to the lows array and cut every adjacent from pos_list
        #Otherwise, put every adjacent on list and set as in queue
        adjs = getAdjs(next_, size_line, size_list)
        if(isMinimum(next_, adjs, number_list)):
            #value: position
            lows[next_] = number_list[next_]
            pos_list = cutAdjs(adjs, pos_list)
        else:
            for p in adjs:
                if(pos_list[p] != 0):
                    continue
                queue.append(p)
                pos_list[p] = 1
                
        #Cut value and remove from queue
        pos_list[next_] = -1
        queue = queue[1:]

    return lows

def getBaisin(low_point, list_, size_line):
    queue = [low_point]
    flagged_queue = []
    baisin = []

    while(True):
        if(len(queue) == 0):
            return baisin
        value = queue[0]
        
        adjs = getAdjs(value, size_line, len(list_))
        for p in adjs:
            if((list_[p] > list_[value]) and (list_[p] < 9) and (p not in flagged_queue)):
                queue.append(p)
                flagged_queue.append(p)
                
        baisin.append(queue[0])
        queue = queue[1:]

def getTopThreeBaisinsSizes(lows):
    low_pos_list = list(lows.keys())

    number_list , size_line = getPosList()

    big_three = [0, 0, 0]
    for p in low_pos_list:
        baisin = getBaisin(p, number_list , size_line)
        baisin_size = len(baisin)
        if(baisin_size >= big_three[0]):
            big_three[2] = big_three[1]
            big_three[1] = big_three[0]
            big_three[0] = baisin_size
        elif(baisin_size >= big_three[1]):
            big_three[2] = big_three[1]
            big_three[1] = baisin_size
        elif(baisin_size >= big_three[2]):
            big_three[2] = baisin_size

    return big_three

def getPosList():
    with open("Day_9_input_file.txt", 'r') as hmap_txt:
        pos_list = []
        for line in hmap_txt:
            l_str = list(line.rstrip())
            size_line = len(l_str)
            for i in l_str:
                pos_list.append(int(i))
    return pos_list , size_line

lows = findLows()

big_three = getTopThreeBaisinsSizes(lows)

print(big_three[0]*big_three[1]*big_three[2])


