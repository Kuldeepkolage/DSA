class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        revNum = 0
        dup = x

        while x > 0:
            ld = x % 10
            revNum = revNum * 10 + ld
            x = x // 10

        return dup == revNum
