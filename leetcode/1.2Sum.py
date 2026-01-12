from typing import List 

def twoSum(nums: List[int], target: int) -> List[int]:
	# Brute Force tc: O(n^2), SC: O(1)
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target: 
				return i, j 

	# normal 2 pointers approach can't fit here because we need to return the indicies and if we sort them the indicies are loosed 
	nums = sorted(nums)
	# i, j = 0, len(nums) - 1 
	# while i < j:
	# 	res = nums[i] + nums[j]
	# 	if res == target:
	# 		return [i, j] # for indices
	# 		# return [nums[i], nums[j]]  # for values
	# 	if res > target:
	# 		j -= 1
	# 	else:
	# 		i += 1 
	# return [-1, -1]

	# lets use hash map tc: o(N) and SC: o(N)
	hm = {} 
	for i in range(len(nums)):
		find_val = target - nums[i] 
		if find_val in hm:
			return [i, hm[find_val]] 
		hm[nums[i]] = i 

if __name__ == "__main__":
	print(twoSum([3, 2, 4], 6))
	# print(twoSum([2, 7, 11, 15], 9))