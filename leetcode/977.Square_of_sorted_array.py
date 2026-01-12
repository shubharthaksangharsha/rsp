# Time: 13:07
from typing import List 

def sortedSquares(nums: List[int]) -> List[int]:
    # TC: O(N), SC: O(N) since we use extra arrays
    neg, pos = [], []
    # i) create two sep list neg and pos
    for i in nums:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)

    # ii) square them and reverse the neg one 
    pos = [i*i for i in pos] 
    neg = list(reversed([i*i for i in neg]))

    # iii) merge 2 sorted arrays 
    res = [] 
    i, j = 0, 0 
    while i < len(pos) and j < len(neg): 
        if pos[i] <= neg[j]:
            res.append(pos[i])
            i += 1
        else:
            res.append(neg[j])
            j += 1 
    while i < len(pos):
        res.append(pos[i])
        i += 1
    while j < len(neg):
        res.append(neg[j])
        j += 1
    return res 
    

if __name__ == "__main__":
    print(sortedSquares([-4,-1,0,3,10]))