class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [[p, s] for p, s in zip(position, speed)]
        # stack = []
        # for p, s in reversed(sorted(pair)):
        #     stack.append((target - p) / s)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)

        # 1. Combine position and speed, then sort closest-to-target first
        # Python defaults to sorting by the first element (position)
        cars = sorted([[p, s] for p, s in zip(position, speed)], reverse=True)
        
        fleets = 0
        max_time = 0.0  # Tracks the slowest fleet leader ahead
        
        # 2. Process cars from right to left
        for p, s in cars:
            time_to_target = (target - p) / s
            
            # If the current car takes MORE time than the fleet leader ahead,
            # it forms a brand-new fleet.
            if time_to_target > max_time:
                fleets += 1
                max_time = time_to_target
                
        return fleets