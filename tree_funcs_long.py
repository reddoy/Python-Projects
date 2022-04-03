"""File: tree_funcs_long.py

   Author: Rohan O'Malley

   Purpose: The purpose of this program is to test different
   aspects of Trees. Program builds 9 functions. First function,
   searches through a bst and returns a node when it is equal to 
   the value passed. Second, searches through a tree and returns 
   the node where value is the same. Third, goes through a BST 
   and finds a place to insert a value passed in. The fourth, fifth
   and sixth functions print out the values in pre, post, and in order
   traversals. Seventh, returns an array of all the values in a Tree
   in in order traversal form. Eigth, goes through a BST and returns
   the max value. Ninth, goes through a Tree and returns the max value
"""
import tree_node
def bst_search_loop (root, val):
    '''
    Function takes a tree and a value and loops
    through nodes in a list till the node and value
    are equal and then that node is returned

    Params:
        - root - a reference to a tree
        - val - an integer 
    Returns:
        - returns the node in the tree if the 
        value is the same as val
        - returns None if value is not found in 
        list
    '''
    if root is None:
        return None
    cur = root
    while cur is not None:
        if cur.val == val:
            return cur
        elif cur.val > val:
            cur = cur.left
        elif cur.val < val:
            cur = cur.right


def tree_search (root, val):
    '''
    Function takes a Tree and recurses through each
    node until it finds the node that is equal to the 
    value passed in as val, then returns that node

    Params:
        - root - a reference to a Tree
        - val - an integer
    Returns:
        - returns None is root is none
        - returns root if val is found in the tree
    '''
    if root is None:
        return None
    if root.val == val:
        return root
    ret_node = tree_search(root.left, val)
    if ret_node is None:
        ret_node = tree_search(root.right, val)
    if ret_node is None:
        return None
    elif ret_node.val == val:
        return ret_node

def bst_insert_loop (root,val):
    '''
    Function searches through a BST with a loop
    then finds a place to insert a value passed in

    Params:
        - root - a reference to a Tree
        - val - an integer
    '''
    cur = root
    while cur is not None:
        if cur.val > val:
            if cur.left is None:
                cur.left = tree_node.TreeNode(val)
                break
            else:
                cur = cur.left
        elif cur.val < val:
            if cur.right is None:
                cur.right = tree_node.TreeNode(val)
                break
            else:
                cur = cur.right


def pre_order_traversal_print (root):
    '''
    Function recurses through tree and
    prints out values of Tree in 
    pre order format

    Params:
        - root - a reference to a Tree
    Returns:
        - returns None if root is None
    '''
    if root is None:
        return None
    print(root.val)
    pre_order_traversal_print(root.left)
    pre_order_traversal_print(root.right)

def in_order_traversal_print (root):
    '''
    Function recurses through tree and
    prints out values of Tree in 
    in order format

    Params:
        - root - a reference to a Tree
    Returns:
        - returns None if root is None
    '''
    if root is None:
        return None
    in_order_traversal_print(root.left)
    print(root.val)
    in_order_traversal_print(root.right)

def post_order_traversal_print (root):
    '''
    Function recurses through tree and
    prints out values of Tree in 
    post order format

    Params:
        - root - a reference to a Tree
    Returns:
        - returns None if root is None
    '''
    if root is None:
        return None
    post_order_traversal_print(root.left)
    post_order_traversal_print(root.right)
    print(root.val)

def in_order_vals(root):
    '''
    Function recurses through a Tree and 
    in in order transversal then takes all
    of the values then all the values are 
    returned in an array.

    Params:
        - root - a reference to a Tree
    Returns:
        - returns an empty array if root is None
        - returns an array of all the values
    '''
    if root is None:
        return []
    else:
        return in_order_vals(root.left) + [root.val] + in_order_vals(root.right)

def bst_max (root):
    '''
    Function recurses through a BST
    and returns the max value

    Params:
        - root - a reference to a BST
    Returns:
        - returns node of the max value in the list
    '''
    if root.right is None:
        return root.val
    else:
        return bst_max(root.right)

def tree_max (root):
    '''
    Function recurses through a Tree
    and returns the max value

    Params:
        - root - a refernce to a Tree
    Returns:
        - returns the max value of the Tree
    '''
    if root is None:
        return None
    else:
        big_val = root.val
        if root.right is not None:
            val = tree_max(root.right)
            if val > big_val:
                big_val = val
        if root.left is not None:
            val = tree_max(root.left)
            if val > big_val:
                big_val = val
        return big_val
