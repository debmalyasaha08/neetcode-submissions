class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        def canship(m):
            day_count = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > m:
                    day_count += 1
                    current_weight = w
                else:
                    current_weight += w
            return day_count <= days
            
        while l < r:
            m = (l + r) // 2
            if canship(m):
                r = m
            else:
                l = m + 1
                
        return l
        

     
        
                
        

