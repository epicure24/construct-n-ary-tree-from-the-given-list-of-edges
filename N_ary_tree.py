class Node:
    def __init__(self,val):
        self.val = val
        self.children =[]
        
#convert the edge list into dictionary

def createDict(edges, root):
    graph ={}
    for x,y in es:
        graph.setdefault(x,set()).add(y)
        graph.setdefault(y,set()).add(x)
    tree, stack = {}, [s]
    while stack:
        parent = stack.pop()
        children = graph[parent] - tree.keys()
        tree[parent] = list(children)
        stack.extend(children)
    for i in tree.keys():
        if tree[i] == []:    """if the node is leaf node, we will give it a 0 value 
           tree[i].append(0)    for my following code to run properly"""
    return tree


# code to convert dictionary into tree

def createNode(tree, root,b=None, stack=None):
    if stack is None:
        stack = []           #stack to store children values
        root = Node(root)    #root node is created
        b=root               #it is stored in b variable 
    x = root.val             # root.val = 2 for the first time
   if len(tree[x])>0 :       # check if there are children of the node exists or not
      for i in range(len(tree[x])):   #iterate through each child
          y = Node(tree[x][i])        #create Node for every child
          root.children.append(y)     #append the child_node to its parent_node
          stack.append(y)             #store that child_node in stack
          if y.val ==0:     #if the child_node_val = 0 that is the parent = leaf_node 
             stack.pop()    #pop the 0 value from the stack
      if len(stack):        #iterate through each child in stack
          if len(stack)>=2:      #if the stack length >2, pop from bottom-to-top
              p=stack.pop(0)     #store the popped val in p variable
          else:
              p = stack.pop()    #pop the node top_to_bottom
      createNode(tree, p,b,stack)   # pass p to the function as parent_node 
return b                            # return the main root pointer
    

#for printing tree  level-wise 

def printLevel(node):
    if node is None:
        return
    queue = []
    queue.append(node)
    while(len(queue)>0):
        n =len(queue)
        while(n>0):
            p = queue[0]
            queue.pop(0)
            if p.val !=0:
                print(p.val, end='  ')
            for ind, value in enumerate(p.children):
                queue.append(value)
            n -= 1
        print(" ")
 
 
edges =[[1,2], [2,4], [2,5], [5,6], [1,3], [3,7], [3,8], [8,9]]
root = 1
tree = createDict(edges, root)      #tree= {1: [2, 3], 3: [8, 7], 7: [0], 8: [9], 9: [0], 2: [4, 5], 5: [6], 6: [0], 4: [0]}
print("the Tree is ", tree)
root_n = createNode(tree, root)
printLevel(root_n)  

output is  
1   
2  3   
4  5  8  7   
6  9 
