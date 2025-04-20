class Loops:
    def __init__(self, n, loopType):
        self.n = n
        self.loopType = loopType

    def startLoop(self):
        if self.loopType == 'for':
            for i in range(self.n):
                print('for :: ' ,i)
            else:
                print('for executed')
        elif self.loopType == 'while':
            i=0
            while i < self.n:
                print('while :: ' ,i)
                i=i+1
            else:
                print('while executed')

loops = [Loops(3,'for'),Loops(5,'while')]
for loop in loops:
    loop.startLoop()

