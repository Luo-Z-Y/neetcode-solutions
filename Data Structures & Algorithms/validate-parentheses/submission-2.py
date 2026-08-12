from collections import deque
class Solution:

    def isValid(self, s: str) -> bool:

        bracket_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }


        bracket_queue = deque()

        for c in s:
            if c == "(" or c == "[" or c == "{":
                bracket_queue.append(c)

            elif bracket_queue and c == bracket_dict[bracket_queue.pop()]:
                continue
            else:
                return False
        
        return True if not bracket_queue else False

        