class Node:
    def __init__(self, key):
        self.key=key
        self.child=[]
    
def new_node(key):
    temp=Node(key)
    return temp

def find_depth_of_tree(ptr):
    '''This functions finds the depth of a N-ary tree
    ptr-points to the root node initially'''
    
    if ptr is None:
        return 0
    for child in ptr.child:
        max_depth=max(max_depth, find_depth_of_tree(ptr.child))
    return max_depth+1
    max_depth=0


#function to find the depth of a given node in a binary tree
def find_depth_of_node(root, x):
    if root==None:
        return -1
    
    dist=-1
    if (root.data==x):
        return dist+1
    
    dist=find_depth_of_node(root.left, x)
    if dist>=0:
        return dist+1
    dist=find_depth_of_node(root.right, x)
    if dist>=0:
        return dist+1
    return dist

def calc_height(root,x):
    global height
    left=0
    right=0
    
    if root == None:
        return -1
    
    leftHeight= calc_height(root.left,x)
    rightheight=calc_height(root.right,x)
    
    ans=max(leftHeight, rightheight)+1
    #left=max(left, leftHeight)
    #right=max(right, rightheight)
    
    if root.data==x:
        height=ans
    
    return ans

def return_height(root, x):
    global height
    
    
    maxheight=calc_height(root,x)
    
    return height
class Node:
   
    def __init__(self, data):
       
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def search_node(root, x):
        if root is None:
            return False
        if root.data == x:
            return True
        return Node.search_node(root.left, x) or Node.search_node(root.right, x)
    



def  calc_level(node, x, level):
    if node==None:
        return 0
    if node.data==x:
        return level
    downlevel=calc_level(node.left, x, level+1)
    if downlevel!=0:
        return downlevel
    downlevel=calc_level(node.right, x, level+1)
    return downlevel

def return_Level(node, data):
    return calc_level(node, data, 1)


def find_parent_of_tree(root,x):
    if root.left.data==x or root.right.data==x:
        return root.data
    return find_parent_of_tree(root.left, x) or find_parent_of_tree(root.right, x)

#def find_diameter_of_tree(root,x):    


def return_diameter(root, x):
    '''global height
    global diam
    
    if root == None:
        return -1
    
    leftHeight= return_diameter(root.left,x)
    rightheight= return_diameter(root.right,x)
    
    ans=max(leftHeight, rightheight)+1
    
    print('dia='+str(dia)+' '+'data='+str(root.data)+' '+"leftheight="+' '+str(leftHeight)+' '+"rightheight="+str(rightheight)+ 'ans='+str(ans))
    
    #left=max(left, leftHeight)
    #right=max(right, rightheight)'''
 
    
    if root.data==x:
        p=root.left.data
        q=root.right.data
        print(p)
        print(q)
    #print(return_height(root, p)+return_height(root, q))
    
def find_sibling_of_a_node(root):
    res = {}
    
    if root is None:
        return res
    
    if root.left is None or root.right is None:
        return res
        
    if root.left is not None and root.right is not None:
        ans = [root.left.data, root.right.data]
        res[root.data] = ans
        
    left_siblings = find_sibling_of_a_node(root.left)
    right_siblings = find_sibling_of_a_node(root.right)
    
    res.update(left_siblings)
    res.update(right_siblings)
    
    return res


    
    

    

    
root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.left.right.right = Node(45)
root.right.left = Node(30)
root.right.right = Node(35)


#print(find_parent_of_tree(root, 3))
#print(find_diameter_of_tree(root,45))
#print(return_diameter(root, 15))
print(find_sibling_of_a_node(root))

        

