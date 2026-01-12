from typing import List 

def three_sum_closest(nums: List[int], target: int) -> int:
	min_diff, res_sum = 1e7, 0
	nums = sorted(nums)
	i = 0 
	while i < len(nums) - 2:
		find_target = target - nums[i]
		j, k = i + 1, len(nums) - 1 
		while j < k:
			curr_sum = nums[i] + nums[j] + nums[k]
			values = (nums[i], nums[j], nums[k])  
			curr_diff = abs(target - curr_sum)
			if curr_diff < min_diff:
				min_diff = curr_diff  
				res_sum = curr_sum
			if nums[j] + nums[k] == find_target:
				return nums[i] + nums[j] + nums[k]
			elif nums[j] + nums[k] > find_target: 
				k -= 1 
			else:
				j += 1 
		i += 1
	return res_sum

if __name__ == "__main__":
	nums = [-1,0,1,2,-1,-4]
	# nums = [0, 0, 0]
	nums = [-2, 0, 1, 1, 2]
	nums = [-1,2,1,-4]
	print(three_sum_closest(nums, 1))