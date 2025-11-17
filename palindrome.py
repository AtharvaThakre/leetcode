class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x >= 10*div:
            div *= 10

        while x:
            right = x // div
            left = x % 10
            if right != left:
                return False
            x = (x % div) // 10
            div = div // 100
        return True


