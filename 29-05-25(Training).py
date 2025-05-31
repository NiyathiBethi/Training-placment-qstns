#problems on Trees:
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)

#Write Function To Find sum of all nodes:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sum_of_nodes(root):
        if root is None:
            return 0
        return root.data+sum_of_nodes(root.left)+sum_of_nodes(root.right)
root=Node(5)
root.left=Node(2)
root.right=Node(6)
print("sum of all nodes:",sum_of_nodes(root))

root=Node(5)
root.left=Node(2)

#Sum of even Nodes:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sum_of_even_nodes(root):
    if root is None:
        return 0
    even_sum=root.data if root.data %2==0 else 0
    return even_sum+sum_of_even_nodes(root.left)+sum_of_even_nodes(root.right)
root=Node(10)
root.left=Node(15)
root.right=Node(20)
root.left.left=Node(25)
root.left.right=Node(30)
print(sum_of_even_nodes(root))

#Sum of Odd Nodes:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sum_of_odd_nodes(root):
    if root is None:
        return 0
    odd_sum=root.data if root.data %2!=0 else 0
    return odd_sum+sum_of_odd_nodes(root.left)+sum_of_odd_nodes(root.right)
root=Node(10)
root.left=Node(15)
root.right=Node(20)
root.left.left=Node(25)
root.left.right=Node(30)
print(sum_of_odd_nodes(root))

#Print all Leaf Nodes in BST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def print_leaf(self):
        if self.left is None and self.right is None:
            print(self.data,end=" ")
        if self.left:
            self.left.print_leaf()
        if self.right:
            self.right.print_leaf()
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.print_leaf())

#Print prime Nodes in BST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def prime(self):
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        if is_prime(self.data):
            print(self.data,end=" ")
        if self.left:
            self.left.prime()
        if self.right:
            self.right.prime()
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.prime())

#kth Largest:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def klargest(self,k):
        def inorder(node,l):
            if node is None:
                return
            inorder(node.right,l)
            l.append(node.data)
            inorder(node.left,l)
        l=[]
        inorder(self,l)
        return l[k-1]
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.klargest(3))

# Top view:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def top_view(root):
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,e=q.pop(0)
        if e not in d:
            d[e]=node.data
        if node.left:
            q.append((node.left,e-1))
        if node.right:
            q.append((node.right,e+1))
    for key in sorted(d):
        print(d[key],end=" ")
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
top_view(root)

#Bottom view:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def bottom_view(root):
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,val=q.pop(0)
        d[val]=node.data
        if node.left:
            q.append((node.left,val-1))
        if node.right:
            q.append((node.right,val+1))
    for key in sorted(d):
        print(d[key],end=" ") 
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
bottom_view(root)





