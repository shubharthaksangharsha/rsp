# TC: O(N), SC: O(1)
from typing import List 

def lengthOfLongestSubstring(s: str)-> int: 	
	low, high,res, hm = 0, 0,-1e6, {}
	while high < len(s):
		# print(hm)
		hm[s[high]] = hm.get(s[high], 0) + 1 
		while hm[s[high]] > 1:
			hm[s[low]] = hm.get(s[low], 0) - 1 
			if hm[s[low]] == 0:
				hm.pop(s[low], None)  
			low += 1
		curr_length = high - low + 1 
		res = max(res, curr_length) 
		high += 1
	return res if res != -1e6 else 0
	
if __name__ == "__main__":
	print(lengthOfLongestSubstring("abcabcbb"))
	print(lengthOfLongestSubstring("bbbbb"))
	print(lengthOfLongestSubstring("pwwkew"))
