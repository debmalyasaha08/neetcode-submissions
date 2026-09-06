class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for c in asteroids:
            while stack and c < 0 and stack[-1] > 0:
                collision = c + stack[-1]
                if collision < 0:
                    stack.pop()
                elif collision > 0:
                    c = 0
                else:
                    c = 0
                    stack.pop()
            if c:
                stack.append(c)
        return stack