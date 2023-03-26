#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sSet = set()
        maxLength = 0
        currentLength = 0
        start = 0

        for i, char in enumerate(s):
            while char in sSet:
                sSet.remove(s[start])
                start += 1
                currentLength -= 1
            sSet.add(char)
            currentLength += 1
            maxLength = max(currentLength, maxLength)
        return maxLength
