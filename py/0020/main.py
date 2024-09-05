class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for item in s:
            if item in pairs:
                if not stack or pairs[item] != stack.pop():
                    return False
            else:
                stack.append(item)
        return not stack
