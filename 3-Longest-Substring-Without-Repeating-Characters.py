class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        counter = 0
        temp = []

        length = len(s)

        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            for l in range(length - 1):
                temp.append(s[l])
                counter = 1

                for r in range(l + 1, length):
                    if s[r] not in temp:
                        temp.append(s[r])
                        counter += 1

                        if r + 1 == length:
                            temp = []
                            if counter > max:
                                max = counter
                        
                            break
                    else:
                        temp = []
                        if counter > max:
                            max = counter
                        break
        
            return max