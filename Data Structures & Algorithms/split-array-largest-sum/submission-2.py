class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def Cansplit(largest):
            subarray = 0
            currsum = 0
            for n in nums:
                currsum += n
                if currsum > largest:
                    subarray += 1
                    currsum = n
            return subarray + 1 <= k
        
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if Cansplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res