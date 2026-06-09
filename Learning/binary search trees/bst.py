class Node() :
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
    
    
class Tree():
    def __init__(self):
        self.root = None
        
    def _insert(self, value, node : Node) : 
        if value <= node.data:
            if node.left: self._insert(value, node.left)
            else: node.left = Node(value)
            
        else : 
            if node.right : self._insert(value , node.right)
            else : node.right = Node(value)
             
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            
        else : self._insert(value, self.root)
        
    def search(self, value, node : Node):
        if not node : return 
        
        if value == node.data:
            return "Found the target"
            
        if value < node.data:
           return self.search(value, node.left)
            
        return self.search(value, node.right)
        
        
            
        
    def inOrder(self, node : Node) :
        #start at root, visit the left, root, right
        if not node: return
        self.inOrder(node.left)
        print(node.data, end = ", ")
        self.inOrder(node.right)
    
    def preOrder (self, node : Node) : 
        if not node : return 
        print(node.data, end = ", ")
        self.preOrder(node.left)
        self.preOrder(node.right)
    
    def postOrder (self, node : Node) : 
        if not node : return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end= ", ")
        
        
    def print(self, flag : str):
        if flag == "in":
            self.inOrder(self.root)
            print("")
        
        elif flag == "pre":
            self.preOrder(self.root)
            print("")
            
        elif flag == "post":
            self.postOrder(self.root)
            print()
        else :
            print ("Invalid flag")


mt = Tree()
mt.insert(10)
mt.insert(20) 
mt.insert(5)
mt.insert(6)
mt.insert(12)
mt.insert(30)
mt.insert(7)
mt.insert(17)
# mt.print("in")
# mt.print("pre")
# mt.print("post")

print(mt.search(7, mt.root))