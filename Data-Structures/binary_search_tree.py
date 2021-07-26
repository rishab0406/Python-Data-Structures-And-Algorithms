class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree():
    def __init__(self,root):
        self.root=Node(root)

    def insert(self,value):
        self.insert_helper(self.root,value)

    def insert_helper(self,cur,value):
        if cur.data < value:
            if cur.right:
                self.insert_helper(cur.right,value)
            else:
                cur.right=Node(value)
        else:
            if cur.left:
                self.insert_helper(cur.left,value)
            else:
                cur.left=Node(value)

    def search(self,value):
        return self.search_helper(self.root,value)
    
    def search_helper(self,cur,value):
        if cur:
            if cur.data == value:
                return True
            elif cur.data < value:
                return self.search_helper(cur.right,value)
            else:
                return self.search_helper(cur.left,value)


bst = BinarySearchTree(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))