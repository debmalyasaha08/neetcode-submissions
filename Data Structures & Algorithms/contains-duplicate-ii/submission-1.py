class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            # 1. Check if the actual value (nums[i]) is already in the window
            if nums[i] in window:
                return True
                
            # 2. Add the actual value to your window
            window.add(nums[i])
            
            # 3. Slide the window: remove the oldest item when size exceeds k
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False
