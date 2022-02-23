# Remove Duplicates from Sorted Arrays
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        size = len(nums)
        if size<2:
            return size
        for i in range (1 , size):
            if nums[i]!=nums[count] :
                count=count+1
                nums[count] = nums[i]
        return count+1