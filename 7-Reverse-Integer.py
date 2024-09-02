class Solution:
    def reverse(self, x: int) -> int:
        isMinus = x < 0

        s = str(abs(x))[::-1]

        result = int(s) * (-1 if isMinus else 1)
        
        if result < (-2 ** 31) or result > (2 ** 31) - 1:
            return 0
        else:
            return result