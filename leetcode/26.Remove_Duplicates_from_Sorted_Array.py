# TIME: 14:29 mins 
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    # Using 2pointers TC: O(N), SC: O(1) 
    # Example using CM nd Officer approch 
    # cm nd officer hvae to assing plot to ecah individul 
    # officers stands on first house, nd cm walk on ech house nd check whether each house is same or not? 
    # if house is diff then cm put that house next to officer and officer stand on new house nd cm keep walking till it dont end 
        i, j = 0, 1 
        while j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i + 1] = nums[j] 
                i += 1 
            j += 1 
        return i + 1


if __name__ == "__main__":
    print(removeDuplicates([1, 2, 3, 4, 4, 5, 6, 6]))