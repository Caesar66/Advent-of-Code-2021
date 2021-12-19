class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        
        self.opening = ['(', '[', '{', '<']
        self.closing = [')', ']', '}', '>']
        
        self.points_corrupted = {')':3, ']':57, '}': 1197, '>': 25137}
        self.points_incomplete = {')':1, ']':2, '}': 3, '>': 4}

    def isEmpty(self):
        return True if self.size == 0 else False

    def push(self, char):
        self.stack.append(char)
        self.size += 1

    def pop(self):
        self.stack.pop(-1)
        self.size -= 1

    def isOpposition(self, char):
        for i in range(len(self.opening)):
            if(self.getOpposition(self.stack[-1]) == char):
                return True
        return False

    def corruption(self, char):
        if self.isClosing(char)== True and self.isOpposition(char) == False:
            return True
        return False

    def isClosing(self, char):
        for s in self.closing:
            if char == s:
                return True
        return False

    def getOpposition(self, char):
        if(char == '('):
           return ')'
        elif(char == '['):
           return ']'
        elif(char == '{'):
           return '}'
        elif(char == '<'):
           return '>'

    def getScore(self, type_, char=None):
        if type_ == 'c':
            return self.points_corrupted[char]
        elif type_ == 'i':
            score = 0
            for s in range(len(self.stack)-1, -1, -1):
                score = score*5 + self.points_incomplete[self.getOpposition(self.stack[s])]
            return score
        
def getSyntaxList(input_file):
    with open(input_file, 'r') as file:
        syntax_str_list = file.readlines()
    
    return [syntax_list.rstrip() for syntax_list in syntax_str_list]

def checkSyntaxCorrupted(syntax_list):
    stack = Stack()
    for symbol in syntax_list:
        if stack.isClosing(symbol) == False:
            stack.push(symbol)
        else:
            if stack.corruption(symbol) == True:
                return stack.getScore(symbol, 'c')
            else:
                stack.pop()
    return 0

def checkSyntaxIncomplete(syntax_list):
    stack = Stack()
    for symbol in syntax_list:
        if stack.isClosing(symbol) == False:
            stack.push(symbol)
        else:
            if stack.corruption(symbol) == True:
                return 0
            else:
                stack.pop()
    if stack.isEmpty() == False:
        return stack.getScore('i')
    return 0

def main(syntax_list):
    score = []
    for l in syntax_list:
        temp = checkSyntaxIncomplete(l)
        if temp != 0:
            score.append(temp)
    score.sort()
    print(score)
    print(score[int((len(score)-1)/2)])
    return None


if __name__ == '__main__':
    input_file = "Day_10_input_file.txt"
    #Day_10_input_file.txt
    syntax_list = getSyntaxList(input_file)
    print(syntax_list)
    main(syntax_list)
