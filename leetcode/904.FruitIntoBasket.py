# TC: O(N), SC: O(1)
from typing import List 

def totalFruit(fruits: List[int])-> int: 	
	low, high,res, hm = 0, 0, 0, {}
	while high < len(fruits):
		# print(hm)
		hm[fruits[high]] = hm.get(fruits[high], 0) + 1 
		while len(hm) > 2:
			hm[fruits[low]] = hm.get(fruits[low], 0) - 1 
			if hm[fruits[low]] == 0:
				hm.pop(fruits[low], None)  
			low += 1
		curr_length = high - low + 1 
		res = max(res, curr_length) 
		high += 1
	return res
	
if __name__ == "__main__":
	print(totalFruit([1, 2, 1]))
	print(totalFruit([0, 1, 2,2]))
	print(totalFruit([1, 2, 3, 2, 2]))
