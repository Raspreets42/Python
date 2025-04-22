class GenericTree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self, childNode):
        childNode.parent = self
        self.children.append(childNode)
    
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
        
    def printTree(self):
        print()
        spaces = ' ' * self.getLevel() * 5
        prifix = spaces + '|----' if self.parent else ""
        print(prifix + self.data)
        for child in self.children:
            child.printTree()

            
    def find(self, value):
        if self.data == value:
            return self
        for child in self.children:
            found = child.find(value)
            if found:
                return found
        return None
    
        
def buildTree():
    root = GenericTree("Electronics")

    laptop = GenericTree("Laptop")
    laptop.addChild(GenericTree("Dell"))
    laptop.addChild(GenericTree("HP"))

    mobile = GenericTree("Mobile")
    mobile.addChild(GenericTree("Samsung"))
    mobile.addChild(GenericTree("OnePlus"))

    root.addChild(laptop)
    root.addChild(mobile)
    
    return root
        
root = buildTree()
root.printTree()
found = root.find("Laptop")
if found:
    print("--------------------------")
    print("|  Parent : ", found.parent.data if found.parent else "" )
    print("|  Data : ", found.data )
    print("|  Childs : ", end="")
    ch = []
    if len(found.children) > 0:
        for c in found.children: 
            ch.append(c.data)
    print(ch)
    print("|_________________________")
else:
    print("Not Found")

