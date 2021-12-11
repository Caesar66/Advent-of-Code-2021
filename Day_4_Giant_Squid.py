class Table:
    def __init__(self, table, position, line_size, column_size):
        self.table_pos = dict(table)
        self.table_marks = dict(table)
        self.position = position
        self.size = (line_size, column_size)
        self.lines = [0]*line_size
        self.columns = [0]*column_size

        self.score = 0
        self.active = True

    def checkNumber(self, number):
        return self.table_pos.get(number)

    def increment(self, pos):
        self.lines[int(pos/self.size[1])] += 1
        self.columns[pos%self.size[0]] += 1

    def markNumber(self, number):
        self.table_marks[number] = -1

    def checkLines(self):
        for l in self.lines:
            if l == self.size[0]:
                return True
        return False

    def checkColumns(self):
        for l in self.columns:
            if l == self.size[1]:
                return True
        return False

    def calculateScore(self, last_draw):
        values = list(self.table_marks.items())
        score = 0
        for i in values:
            if i[1] != -1:
                score += int(i[0])
        self.score = score*last_draw

    def getScore(self):
        return self.score

    def getActive(self):
        return self.active

    def setInactive(self):
        self.active = False

    def printTable(self):
        return self.table_marks

def getDictionary(list_):
    #We use dictionary to make it faster to find the numbers
    return {list_[i]: i for i in range(len(list_))}

def parseTable(table, pos):
    #Converting the string values to lists
    counter = 1 + pos
    str_ = ""
    while True:
        if counter >= len(tables) or tables[counter] == '':
            break
        str_ += tables[counter]
        str_ += " "
        counter += 1

    return str_.split()

def parseAllTables(tables):
    tables_list = []
    for i in range(len(tables)):
        if tables[i] == '':
            tables_list.append(getDictionary(parseTable(tables, i)))
    return tables_list

def getOrderWinTable(tables, line_size, draws):
    #Create a table object for every table dict
    table_obj_list = []
    p = 0
    for t in tables:
        table_obj_list.append(Table(t, p, line_size, getColumnSize(len(t), line_size)))
        p += 1

    #Check every number in draws and compare to each dictionary
    winning = []
    for number in draws:
        for t in table_obj_list:
             r = t.checkNumber(number)
             #Checks if number exist in the table and if the table is still active (it is active if no column or line is complete yet)
             if ((r != None) and (t.getActive() == True)):
                 t.increment(r)
                 t.markNumber(number)
                 if (t.checkLines() or t.checkColumns()):
                     t.calculateScore(int(number))
                     t.setInactive()
                     winning.append(t)
    return winning

def getColumnSize(table_size, line_size):
    return int(table_size/line_size)
    
with open("Day_4_file_input.txt", 'r') as file:
    draws = file.readline().rstrip().split(',')
    tables = [line.rstrip() for line in file]
    line_size = len(tables[1].split())

winning = getOrderWinTable(parseAllTables(tables), line_size, draws)

print(winning[0].printTable())
print(winning[0].getScore())
print(winning[-1].printTable())
print(winning[-1].getScore())
