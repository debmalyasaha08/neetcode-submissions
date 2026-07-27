class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums

            mid = nums[len(nums) // 2]

            left = [n for n in nums if n < mid]
            middle = [n for n in nums if n == mid]
            right = [n for n in nums if n > mid]

            return quicksort(left) + middle + quicksort(right)
        return quicksort(nums)