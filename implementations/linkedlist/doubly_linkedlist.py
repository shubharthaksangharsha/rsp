from typing import List 
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None  
		self.prev = None


class DLL:
	def __init__(self):
		self.head = None 

	def arr_to_dll(self, arr: List[int]=None) -> None:
		if arr is None:
			return 
		self.head = Node(arr[0])
		if len(arr) == 1:			
			return 
		temp = self.head 
		for i in range(1, len(arr)):
			curr = Node(arr[i]) 
			temp.next = curr 
			curr.prev = temp 
			temp = curr

	def print_dll(self):
		temp = self.head 
		get_data = lambda node: node.data if node else None
		while temp: 
			print(f"{temp.data}" 
				f"|next={get_data(temp.next)}" 
				f"|prev={get_data(temp.prev)}" 
				) 
			temp = temp.next

if __name__ == "__main__":
	dll = DLL() 
	dll.arr_to_dll([1, 2, 3, 4])
	dll.print_dll()