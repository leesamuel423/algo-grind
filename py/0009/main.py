class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0

        while x > reverse:
            reverse = (reverse * 10) + (x % 10)
            x //= 10

        return x == reverse or x == reverse // 10


"""
False when:
    negative number
    ends with 0 (but 0 is True)

reverse = 0

while x > reverse:
    x becomes x // 10

check if x == reverse or reverse // 10 == x
"""
