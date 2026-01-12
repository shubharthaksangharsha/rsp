from typing import List 

def twoSum(nums: List[int], target: int) -> List[int]:
	# Brute Force tc: O(n^2), SC: O(1) # Gives TLE 
	# for i in range(len(nums)):
	# 	for j in range(i + 1, len(nums)):
	# 		if nums[i] + nums[j] == target: 
	# 			return [i+1, j+1]

	# lets use hash map tc: o(N) and SC: o(N)
	# hm = {} 
	# for i in range(len(nums)):
	# 	find_val = target - nums[i] 
	# 	if find_val in hm:
	# 		return sorted([i+1, hm[find_val]])
	# 	hm[nums[i]] = i+1 

	# lets use 2pointers tc: O(N) and SC: o(1) (OPTIMZIED AND BEST SOL)

	i, j = 0, len(nums) - 1 
	while i < j:
		res = nums[i] + nums[j]
		if res == target:
			return [i + 1, j + 1] # for indices
		if res > target:
			j -= 1
		else:
			i += 1 
	return [-1, -1]




if __name__ == "__main__":
	print(twoSum([2, 3, 4], 6))
	# print(twoSum([2, 7, 11, 15], 9))