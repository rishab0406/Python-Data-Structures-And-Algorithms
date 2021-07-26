class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree():
    def __init__(self,root):
        self.root=Node(root)

    def preorder_print(self,node):
        if node:
            print(node.value,end=" ")
            self.preorder_print(node.left)
            self.preorder_print(node.right)
        pass

    def inorder_print(self,node):
        if node:
            self.inorder_print(node.left)
            print(node.value,end=" ")
            self.inorder_print(node.right)
        
        
    def postorder_print(self,node):
       if node:
           self.postorder_print(node.left)
           self.postorder_print(node.right)
           print(node.value,end=" ")

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return(1 + max(left_height, right_height))


    

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print("Pre Order : ",end="")
tree.preorder_print(tree.root)
print()
print("In Order : ",end="")
tree.inorder_print(tree.root)
print()
print("Post Order : ",end="")
tree.postorder_print(tree.root)
print()
print("Height : ",end="")
print(tree.height(tree.root))
