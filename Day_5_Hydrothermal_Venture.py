def getNonDiagonals(segments):
    non_diagonals = []
    for s in segments:
        if s[0][0] == s[1][0] or s[0][1] == s[1][1]:
            non_diagonals.append(s)
    return non_diagonals

def getDiagonals(segments):
    segments_with_diagonals = []
    for s in segments:
        if s[0][0] == s[1][0] or s[0][1] == s[1][1] or abs(s[0][0] - s[1][0]) == abs(s[0][1] - s[1][1]):
            segments_with_diagonals.append(s)
    return segments_with_diagonals

def getSegments(input_file):
    with open(input_file, 'r') as file:
        segments = file.readlines()

    segments = [segments[i].rstrip().split("->") for i in range(len(segments))]

    for i in range(len(segments)):
        for j in range(len(segments[i])):
            segments[i][j] = segments[i][j].split(',')
            for k in range(len(segments[i][j])):
                segments[i][j][k] = int(segments[i][j][k])
    
    return segments

def getPoints(segment):
    initial = segment[0]
    final = segment[1]
    points = []
    #Here we see which coordinate is the equal one, x or y
    if initial[0] == final[0]:
        points.append('x')
        #We will create a list with a nested dictionary
        # [type_coord, {number_coord_type:{number_coord:1, number_coord_2:1, ...}}]
        points.append({initial[0]:{}})
        #Here which coordinate is smaller the one from the second point or first one.
        if initial[1] < final[1]:
            for i in range(initial[1], final[1]+1):
                points[1][initial[0]][i] = 1
        else:
            for i in range(final[1], initial[1]+1):
                points[1][initial[0]][i] = 1
    elif initial[1] == final[1]:
        points.append('y')
        points.append({initial[1]:{}})
        
        if initial[0] < final[0]:
            for i in range(initial[0], final[0]+1):
                points[1][initial[1]][i] = 1
        else:
            for i in range(final[0], initial[0]+1):
                points[1][initial[1]][i] = 1
    else:
        #Doing the diagonals we check four cases:
        #x1 < x2 and y1 < y2
        #x1 < x2 and y1 > y2
        #x1 > x2 and y1 < y2
        #x1 > x2 and y1 > y2
        points.append('d')
        points.append({})
        counter = 0
        if initial[0] < final[0]:
            while(counter+initial[0] <= final[0]):
                if initial[1] < final[1]:
                    points[1][initial[0]+counter] = initial[1]+counter
                else:
                    points[1][initial[0]+counter] = initial[1]-counter
                counter += 1
        else:
            while(counter+final[0] <= initial[0]):
                if initial[1] < final[1]:
                    points[1][final[0]+counter] = final[1]-counter
                else:
                    points[1][final[0]+counter] = final[1]+counter
                counter += 1
    return points

def countPoints(points_list):
    counter = 0
    while points_list:
        coord = points_list.popitem()
        while coord[1]:
            if coord[1].popitem()[1] > 1:
                counter += 1
    return counter

def main(segments, diagonals=False):
    points = {}

    if diagonals == False:
        segments_list = getNonDiagonals(segments)
    else:
        segments_list = getDiagonals(segments)
    for segment in segments_list:
        points_found = getPoints(segment)
        #Checking for type of coordinates, then we insert the coord as key and then the other as values with their counters
        #Iterating through the dict by popping it until it is empty
        
        if points_found[0] == 'x':
            coordinates = points_found[1].popitem()
            while(coordinates[1]):
                if points.get(coordinates[0]) == None:
                    points[coordinates[0]] = {}
                
                y = coordinates[1].popitem()[0]

                if points[coordinates[0]].get(y) == None:
                    points[coordinates[0]][y] = 1
                else:
                    points[coordinates[0]][y] += 1
        elif points_found[0] == 'y':
            coordinates = points_found[1].popitem()
            while(coordinates[1]):
                #Does the same thing as in x but in the "inverse" order
                x = coordinates[1].popitem()[0]
                
                if points.get(x) == None:
                    points[x] = {}

                if points[x].get(coordinates[0]) == None:
                    points[x][coordinates[0]] = 1
                else:
                    points[x][coordinates[0]] += 1
        else:
            coordinates = points_found[1]
            while coordinates:
                x,y = coordinates.popitem()
                if points.get(x) == None:
                    points[x] = {}
                if points[x].get(y) == None:
                    points[x][y] = 1
                else: points[x][y] += 1
                
    print(countPoints(points))
    return None

if __name__ == '__main__':
    input_file = "Day_5_input_file.txt"
    segments = getSegments(input_file)
    #print(segments)
    #print(getNonDiagonals(segments))
    
    main(segments, True)
