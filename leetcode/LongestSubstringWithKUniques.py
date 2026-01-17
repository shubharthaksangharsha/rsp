# TC: O(N), SC: O(1)
from typing import List 

def min_size_k(s: str, k: int) -> int: 
	low, high,res, hm = 0, 0,-1e6, {}
	while high < len(s):
		# print(hm)
		hm[s[high]] = hm.get(s[high], 0) + 1 
		while len(hm) > k:
			hm[s[low]] = hm.get(s[low], 0) - 1 
			if hm[s[low]] == 0:
				hm.pop(s[low], None)  
			low += 1
		
		if len(hm) == k:
			# print("length of hm: ", len(hm))	
			curr_length = high - low + 1 
			
			res = max(res, curr_length) 
			# print(f"low: {low}, high: {high}, curr_length: {curr_length}, res: {res}")
		high += 1
	return res if res != -1e6 else -1
	
if __name__ == "__main__":
	print(min_size_k("aabacbebebe", 3))
