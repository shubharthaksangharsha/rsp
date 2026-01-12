from typing import List

def brute_force(nums: List[int]) -> List[List[int]]: 
	# Triple loop idea TC: O(n^3), SC: O(N^3) (because we are storing all subarrays)
	#[1, 2, 3]
	  i 
	  j
	  k 
	  temp = [1]
	  res = [[1]]

	 #[1, 2, 3]
	  i 
	      j
	      k 
	 temp = [1, 2]
	 res = [[1], [1, 2]]
	 #[1, 2, 3]
	  i 
	         j
	  	  k 
	  temp = [1, 2, 3]
	  res = [[1], [1, 2], [1, 2, 3]]

	  #[1, 2, 3]
	       i 
	          j
	  	  	  k 
	  temp = [2]
	  res = [[1], [1, 2], [1, 2, 3], [2]]

	  #[1, 2, 3]
	       i 
	          j
	  k 
	  temp = [2, 3]
	  res = [[1], [1, 2], [1, 2, 3], [2], [2, 3]]

	  #[1, 2, 3]
	       	  i 
	            j
	          k 
	  temp = [3]
	  res = [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
	res, n  = [], len(nums)
	for i in range(n):
		for j in range(i, n):
			temp = [] 
			for k in range(i, j+1):
				temp.append(nums[k]) 
			res.append(temp) 
	return res

def better_approach(nums: List[int]) -> List[List[int]]:
	# Using slicing or grow window TC: O(N^2), SC: O(N^3) Total elements are N^3 / 2 
	res, n = [], len(nums)
	for i in range(n):
		curr = [] 
		for j in range(i, n):
			curr.append(nums[j])  # grow the window 
			res.append(curr.copy()) 
	return res 

# def prefix_sum(nums: List[int]) -> List[List[int]]:
# 	# TC: O(N), SC: O(N) 
# 	n = len(nums)
# 	prefix = [0] * n 
# 	prefix[0] = nums[0] 

# 	res = []
# 	for i in range(1, n):
# 		prefix[i] = prefix[i-1] + nums[i] 
# 	for i in range(n):
# 		for j in range(i, n):
# 			if i == 0:
# 				# print(prefix[j])
# 				res.append(prefix[j])
# 			else:
# 				# print(prefix[j] - prefix[i-1])
# 				res.append(prefix[j] - prefix[i-1])
	return res 
if __name__ == "__main__":
	print(brute_force([1, 2, 3]))
	print(better_approach([1, 2, 3]))