class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        target =  len(nums) // 3
        res = []
        for n in nums:
            count[n] = count.get(n,0) + 1
        for n, c in count.items():
            if c > target:
                res.append(n)
        return res