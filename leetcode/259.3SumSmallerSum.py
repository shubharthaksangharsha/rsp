from typing import List 

def three_sum_smaller_sum(nums: List[int], target: int) -> int:
	res = 0 
	nums = sorted(nums)
	i = 0 
	while i < len(nums) - 2:
		find_target = target - nums[i]
		j, k = i + 1, len(nums) - 1 
		while j < k:
			curr_sum = nums[i] + nums[j] + nums[k]
			if curr_sum < target:
				res += (k - j)
				j += 1 
			else:
				k -= 1 
		i += 1
	return res

if __name__ == "__main__":
	nums = [-1,0,1,2,-1,-4]
	# nums = [0, 0, 0]
	nums = [-2, 0, 1, 1, 2]
	nums = [-1,2,1,-4]
	nums = [-2, 0, 1, 3] 
	print(three_sum_smaller_sum(nums, 2))