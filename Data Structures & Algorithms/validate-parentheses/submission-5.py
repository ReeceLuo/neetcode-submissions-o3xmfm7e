class Solution:
    def isValid(self, s: str) -> bool:
        # 3 parentheses pairs
        # if close bracket, top most must be matching open bracket
        # if close bracket and empty -> false
        
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != closeToOpen[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0

