class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        # so we can rank the positions from closest to farthest, if the farther cars can reach the destination at a short time, it's part of the larger fleet

        combined = [[i, j] for i, j in zip(position, speed)]
        #Since Python automatically sorts lists of lists by their first element by default, you can actually achieve the exact same result even more simply by omitting the key entirely: combined = sorted(combined, reverse=True).
        combined = sorted(combined, key=lambda x: x[0], reverse=True)
        
        for c in combined:
            if not stack:
                stack.append(c)
                continue
            time_cur = (target - c[0]) / c[1]
            time_fleet = (target - stack[-1][0]) / stack[-1][1]
            if time_cur > time_fleet:
                stack.append(c)
        return len(stack)


