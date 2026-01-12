from typing import List 

def max_sum(nums: List[int], k: int) -> int: 
	low, high, curr_sum, res = 0, k - 1, 0, -1e6 
	for i in range(low, high + 1):
		curr_sum += nums[i] 
	while high < len(nums):
		res = max(res, curr_sum) 
		low += 1 
		high += 1 
		curr_sum -= nums[low - 1] 
		if high == len(nums):
			break 
		curr_sum += nums[high] 
	return res 

if __name__ == "__main__":
	print(max_sum([100, 200, 300, 400], 2))
