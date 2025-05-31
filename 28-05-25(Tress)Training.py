# 496. Next Greater Element I-----LEETCODE
nums1=[4,1,2]
nums2=[1,3,4,2]
dict={n:i for i,n in enumerate(nums1)}
res=[-1]*len(nums1)
stack=[]
for i in range(len(nums2)):
    curr=nums2[i]
    while stack and curr>stack[-1]:
        val=stack.pop()
        index=dict[val]
        res[index]=curr
    if curr in dict:
        stack.append(curr)
print(res)


# 901. Online Stock Span
class StockSpanner:
   def _init_(self):
       self.stack=[]
   def next(self, price: int) -> int:
       span=1
       while self.stack and self.stack[-1][0]<=price:
           span+=self.stack.pop()[1]
       self.stack.append((price,span))
       return span
    

# Binary Search Tree Traversal   
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if key<root.val:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)


def preOrder(root):
    if root is None:
        return
    print(root.val,end=" ")
    preOrder(root.left)
    preOrder(root.right)


def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val,end=" ")
    

# Level Order Traversal----- HACKER RANK
def levelOrder(root):
    q=[]
    q.append(root)
    while len(q)!=0:
        rt=q.pop(0)
        print(rt.val,end=" ")
        if rt.left is not None:
            q.append(rt.left)
        if rt.right is not None:
            q.append(rt.right)
c=Node(7)
c=insert(c,key=3)
c=insert(c,key=5)
c=insert(c,key=2)
c=insert(c,key=6)
inorder(c)
preOrder(c)
postOrder(c)
levelOrder(c)


#Is This a Binary Search Tree?------------HACKER RANK
def check_binary_search_tree_(root):
    res=[]
    def inOrder(root):
        if root is None:
            return
        inOrder(root.left)
        res.append(root.data)
        inOrder(root.right)
    inOrder(root)
    for i in range(len(res)-1):
        if res [i]>=res[i+1]:
            return False
    return True

# Height of a Binary Tree----HACKER RANK
def height(root):
    if root is None:
        return -1
    left=height(root.left)
    right=height(root.right)
    return max(left,right)+1


# topview-------HACKER RANK
def topView(root):
    q=[]
    d=dict()
    root.level=0
    q.append(root)
    while len(q)!=0:
        root=q.pop(0)
        if root.level not in d:
            d[root.level]=root.info
        if root.left is not None:
            q.append(root.left)
            root.left.level=root.level-1
        if root.right is not None:
            q.append(root.right)
            root.right.level=root.level+1
    for key in sorted(d.keys()):
            print(d[key],end=" ")