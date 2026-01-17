# TC: O(N), SC: O(1)
from typing import List 


def min_size_k(s: List[int], k: int )-> int: 	
	low, high, curr_sum, res = 0, 0, 0, 1e6
	while high < len(s):

		curr_sum += s[high] 

		# shrink while sum is enough 

		while curr_sum >= k: 
			res = min(res, high - low + 1) 
			curr_sum -= s[low] 
			low += 1 

		high += 1 

	return res if res != 1e6 else 0

if __name__ == "__main__":
	print(min_size_k([2, 3, 1, 2, 4, 3], 7))
