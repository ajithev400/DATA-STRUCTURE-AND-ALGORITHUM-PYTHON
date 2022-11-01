class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        #compare the new value with the parent
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data >self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #print the tree

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
    
    #inorder travers
    #left -> root -> right
    def inorder_traversal(self,root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res
    
    #preorder travers
    #root -> left ->right
    def preorder_traversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    #post Order
    #left -> right -> root
    def postorder_traversal(self,root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.data)
        return res
    
    #find value
    def find_val(self,value):
        if value<self.data:
            if self.left is None:
                return str(value)+" Not Found"
            return self.left.find_val(value)
        elif value > self.data:
            if self.right is None:
                return str(value)+" Not found"
            return self.right.find_val(value)
        else:
            return str(self.data)+' is found'

root = Node(11)
root.insert(3)
root.insert(6)
root.insert(12)
root.insert(2)
root.insert(4)
root.insert(7)
print("Inorder")
print(root.inorder_traversal(root))
print("PreOrder")
print(root.preorder_traversal(root))
print("postorder")
print(root.postorder_traversal(root))
# root.print_tree()
print(root.find_val(11))
print(root.find_val(7))
print(root.find_val(44))

print("Tree")