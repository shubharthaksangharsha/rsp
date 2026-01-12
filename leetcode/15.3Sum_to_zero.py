from typing import List 

def threeSum(nums: List[int]) -> List[List[int]]:
	res = [] 
	nums = sorted(nums)
	i = 0 
	while i < len(nums) - 2:
		if i > 0 and nums[i] == nums[i - 1]:
			i += 1 
			continue
		target = -(nums[i]) 
		j, k = i + 1, len(nums) - 1 
		while j < k: 
			if nums[j] + nums[k] == target:
				res.append([nums[j], nums[k], nums[i]])
				j += 1 
				k -= 1 
				while j < k and nums[j] == nums[j-1]:
					j += 1
				while j < k and nums[k] == nums[k+1]:
					k -= 1 
			elif nums[j] + nums[k] > target: 
				k -= 1 
			else:
				j += 1 
		i += 1
	return res

if __name__ == "__main__":
	nums = [-1,0,1,2,-1,-4]
	# nums = [0, 0, 0]
	nums = [-2, 0, 1, 1, 2]
	print(threeSum(nums))