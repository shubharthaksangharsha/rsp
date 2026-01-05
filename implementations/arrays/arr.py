from typing import List, Optional, Tuple

def populate(arr: List[int], n_elements: int, debug=False) -> Optional[Tuple[List, int]]:  
	"""
	Populate the array with the given size 
	"""
	if n_elements > len(arr): 
		print("Memory exceed!!")
		return
	for i in range(n_elements):
		if debug:
			arr[i] = i + 1
		else:
			arr[i] = int(input(f"{i+1} element: "))
	return arr, n_elements 

def insert_at_begining(arr: List[int], n: int, val: int) ->  Optional[Tuple[List, int]]:  
	if n>= len(arr):
		print("Overflow")
		return 
	i = n 
	while i > 0: 
		arr[i] = arr[i - 1] 
		i -= 1
	arr[0] = val 
	return arr, n + 1 

def insert_at_end(arr: List[int], n: int, val: int) ->  Optional[Tuple[List, int]]:  
	if n >= len(arr): 
		print("Overflow")
		return 
	arr[n] = val 
	return arr, n + 1  

def insert_at(arr: List[int], n: int, pos: int, val: int) -> Optional[Tuple[List, int]]:  
	if n >= len(arr):
		print("Overflow!")
		return 
	if pos < 1 or pos > n + 1:
		print("Invalid pos")
		return 
	i = n
	while i >= pos: 
		arr[i] = arr[i - 1]
		i -= 1 
	arr[pos-1] = val
	return arr, n + 1 

def remove_at(arr: List[int], n: int, pos: int) -> Optional[Tuple[List, int]]: 
	if n <= 0: 
		print("Underflow!")
		return 
	if pos < 1 or pos > n: 
		print("Invalid pos")
		return 
	i = pos - 1 
	while i < n - 1: 
		arr[i] = arr[i + 1] 
		i += 1 
	arr[n-1] = 0
	return arr, n - 1

def remove_at_begining(arr: List[int], n: int) -> Optional[Tuple[List, int]]: 
	if n <= 0:
		print("Underflow!")
		return 
	i = 0 
	while i < n - 1: 
		arr[i] = arr[i + 1] 
		i += 1 
	arr[n - 1] = 0 
	return arr, n - 1 

if __name__ == "__main__":
	n = 10
	arr = [0] * n
	arr, n = populate(arr, 5, debug=True)
	print(arr)
	arr, n = insert_at(arr, n, 2, 10)
	print(arr)
	arr, n = insert_at_end(arr, n, 100)
	print(arr)
	arr, n = insert_at_begining(arr, n, 200)
	print(arr)
	arr, n = remove_at(arr, n, 2)
	print(arr)
	arr, n = remove_at_begining(arr, n)
	print(arr)
	arr, n = remove_at_begining(arr, n)
	print(arr)
	arr, n = remove_at_begining(arr, n)
	print(arr)
	arr, n = remove_at_begining(arr, n)
	print(arr)
	arr, n = remove_at_begining(arr, n)
	print(arr)
	arr, n = remove_at_begining(arr, n)
	print(arr)
	arr, n = remove_at_begining(arr, n)
	print(arr)