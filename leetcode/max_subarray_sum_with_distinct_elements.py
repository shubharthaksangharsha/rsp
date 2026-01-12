from typing import List 
def max_sum(nums: List[int], k: int) -> int: 
	low, high, curr_sum, res, hm = 0, k - 1, 0, -1e6, {}
	for i in range(low, high + 1):
		if nums[i] in hm:
			curr_sum = 0 
			break
		curr_sum += nums[i]
		hm[nums[i]] = True   
	print(low, high, curr_sum, res, hm)
	while high < len(nums):
		res = max(res, curr_sum) 
		low += 1 
		high += 1 
		if nums[low] in hm: 
			low +=1
			hm = {} 
			continue 
		curr_sum -= nums[low - 1] 
		if high == len(nums):
			break 
		curr_sum += nums[high] 
	return res 

if __name__ == "__main__":
	print(max_sum([5,1,4,2,9,9,9], 3))
