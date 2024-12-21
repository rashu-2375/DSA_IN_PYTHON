class Node:
    def __init__(self, element, parent = None):
        self.element = element #Each node contains an element, a reference to its parent node, and references to its left and right children.
        self.parent = parent
        self.lchild = None
        self.rchild = None
class BinaryTree:
    def __init__(self):
        self._root = None

    def add_root(self,e):
        if self._root is None:
            self._root = Node(e)
            return self._root
        else:
            raise ValueError('Root already exists')

    def add_lchild(self,p,e):
        if isinstance(p,Node):
            if p.lchild is None:
                p.lchild = Node(e,p)
            else:
                raise ValueError('Left child already exists')
        else:
            raise ValueError('Invalid parent node')
        
    def add_rchild(self,p,e):
        if isinstance(p,Node):
            if p.rchild is None:
                p.rchild = Node(e,p)
            else:
                raise ValueError('Right child already exists')
        else:
            raise ValueError('Invalid parent node')
        
    def delete(self,p):
        if isinstance(p, Node):
            if p.lchild is None and p.rchild is None:  # Leaf node
                if p.parent.lchild == p:
                    p.parent.lchild = None
                else:
                    p.parent.rchild = None
                element = p.element
                p = None
                return element
            elif p.lchild is None or  p.rchild is None:  # one child
                if p.lchild:
                    child = p.lchild
                else:
                    child = p.rchild
                
                if p.parent:
                    if p.parent.lchild == p:
                        p.parent.lchild = child
                    else:
                         p.parent.rchild = child
                    child.parent = p.parent
                else:
                    self.root = child
                    child.parent = None

                element = p.element
                # p = None
                return element
            
            else: #node has two children, it raises a ValueError because it cannot be deleted without violating the binary tree structure.
                raise ValueError('Node has two children')
        else:
            raise ValueError('Invalid node')
        
    def get_root(self):
        if self._root:
            return self._root.element
        else:
            raise ValueError('Empty tree')
               
    def parent(self, p):
        if isinstance(p, Node) and p.parent:
            return p.parent.element
        else:
            raise ValueError('Invalid root or node is root')
        
    def left(self, p):
        if isinstance(p, Node) and p.lchild:
            return p.lchild.element
        else:
            raise ValueError("Invalid node or node has no left child")
        

    def right(self, p):
        if isinstance(p, Node) and p.rchild:
            return p.rchild.element
        else:
            raise ValueError("Invalid node or node has no right child")

    def num_children(self,p):
        if isinstance(p, Node):
            children = 0
            if p.lchild:
                children += 1
            if p.rchild:
                children += 1
            return children
        
        else:
            raise ValueError('Invalid node')
    
    def __len__(self):
        def count_nodes(node):
            if node is None:
                return 0
            else: #recursively counts the nodes starting from the root node.
                return 1 + count_nodes(node.lchild) + count_nodes(node.rchild)
        
        return count_nodes(self._root)


# create a  new binary tree
tree = BinaryTree()

# Add a root node
root = tree.add_root(10)
print("root =", root)

# Add left and right children to the root
tree.add_lchild(root, 5)
print("left child of root is ", tree.left(root))
tree.add_rchild(root, 15)
print("right child of root is ", tree.right(root))

# Add children to the left child
left_child = root.lchild
tree.add_lchild(left_child, 3)
print()
tree.add_rchild(left_child, 7)

# Add a child to the right child
right_child = root.rchild
tree.add_lchild(right_child, 12)

# Print the number of nodes in the tree
print(len(tree))  # Output: 6

# Print the root element
print(tree.get_root())  # Output: 10

# Print the parent of the left child of the root
print(tree.parent(left_child))  # Output: 10

# Print the left child of the left child of the root
print(tree.left(left_child))  # Output: 3

# Print the right child of the left child of the root
print(tree.right(left_child))  # Output: 7

# Print the number of children of the left child of the root
print(tree.num_children(left_child))  # Output: 2

# Delete the right child of the root
deleted_element = tree.delete(right_child)
print(deleted_element)  # Output: 15




        




        

