from typing import List, Optional
class Node: 
	def __init__(self, data):
		self.data = data 
		self.left = None 
		self.right = None 


prev = None
	
def searchBST(root, val): 
	if root is None: 
		return False 
	if root.data == val: 
		return True
	if root.data > val:
		return searchBST(root.left, val) 
	if root.data < val:
		return searchBST(root.right, val) 
	return False 

def get_node(root, val): 
	if root is None: 
		return 
	if root.data == val: 
		return root 
	if root.data > val:
		return get_node(root.left, val) 
	if root.data < val:
		return get_node(root.right, val) 

	return 

def bst_length(root: Node) -> int: 
	if root is None: 
		return 0 
	return bst_length(root.left) + bst_length(root.right) + 1

def inorderBST(root: Optional[Node]) -> None: 
	if root is None: 
		return 
	if root.left: 
		inorderBST(root.left) 

	print(root.data, end = " ")
	if root.right:
		inorderBST(root.right)

def insertBST(root: Optional[Node], d: int) -> Node:
	if root is None: 
		root = Node(d) 
		return root 

	if d > root.data: 
		root.right = insertBST(root.right, d) 

	if d < root.data: 
		root.left = insertBST(root.left, d) 

	return root 
		
def createBST(arr: List[int]) -> Node:
	root = None 
	for i in arr: 
		root = insertBST(root, i)
	return root 

def delete_bst(root: Node, val: int) -> Optional[Node]: 
	# base case 
	if root is None: 
		return root 
	if root.data == val: 
		# 0 child
		if root.left is None and root.right is None: 
			return None 
		# 1 child 

		# left child 
		if root.left is None:
			return root.right
		# right child 
		if root.right is None:
			return root.left
		# 2 child 
		pred = inorder_precedor(root, root)
		if pred:
			root.data = pred.data 
			root.left = delete_bst(root.left, pred.data)
			return root 
	if root.data > val: 
		root.left = delete_bst(root.left, val)
		return root

	root.right = delete_bst(root.right, val)
	return root 


def inorder_precedor(root: Node, node: Node) -> Optional[Node]: 
	prev = None

	def helper(curr_node: Optional[Node]) -> None:
		nonlocal prev

		if curr_node is None: 
			return    

		if curr_node.left: 
			ans = helper(curr_node.left)
			if ans: 
				return ans 

		if curr_node.data == node.data:
			return prev

		prev = curr_node

		if curr_node.right:
			return helper(curr_node.right)		

		return 						

	return helper(root)

def clear_bst(root: Node) -> None:
	while root is not None:
		root = delete_bst(root, root.data)
	return root 
if __name__ == "__main__":
	root = createBST([100, 50, 20, 70, 160, 200]) 

	# inorder
	inorderBST(root)
	print()
	print(bst_length(root) == len([100, 50, 20, 70, 160, 200]))
	root = clear_bst(root)
	inorderBST(root)
	print()

	# print(searchBST(root, 210))
	# node = get_node(root, 50)

	# print(inorder_precedor(root, node).data)