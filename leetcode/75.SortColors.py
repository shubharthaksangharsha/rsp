from typing import List
def sortColors(nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Brute force I can think is extra space so it is TC: O(N) but SC: O(N)
        # by creating 3 list of 0s, 1s and 2s and then adding each element one by one
        # or we can do one more thing is creating 3 variables and increase the count of each variable
        # TC: O(N) SC: O(1) but still taking 3 variables
        # problem is nothing but it's just it's taking 2 passes

        # zeros, ones, twos = 0, 0, 0
        # for i in nums:
        #     if i == 0:
        #         zeros += 1
        #     elif i == 1:
        #         ones += 1
        #     else:
        #         twos += 1
        # i = 0
        # while i < len(nums):
        #     while zeros:
        #         nums[i] = 0
        #         zeros -= 1
        #         i += 1
        #     while ones:
        #         nums[i] = 1
        #         ones -= 1
        #         i += 1
        #     while twos:
        #         nums[i] = 2
        #         twos -= 1
        #         i += 1

        # Now let's do it in-place, 1 pass, without counting
        # Dutch National Flag Algorithm

        # zeros  = [0 ... low-1]
        # ones   = [low ... mid-1]
        # unknown= [mid ... high]
        # twos   = [high+1 ... end]

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0: # send it to the left zone 
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1: # 1 is already in the correct middle zone 
                mid += 1
            else:  # send it to the right zone
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums 
if __name__ == "__main__":
    nums = sortColors([2, 0, 2, 1, 1, 0])
    print(nums)