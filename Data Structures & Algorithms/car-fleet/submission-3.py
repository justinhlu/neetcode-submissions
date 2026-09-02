class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort()
        stack = []

        for p, s in cars[::-1]:
            time = (target-p) / s

            if len(stack) == 0:
                stack.append(time)
            elif stack and time > stack[-1]:
                stack.append(time)
        
        return len(stack)