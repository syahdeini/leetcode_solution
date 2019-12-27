# 10:12 27-12-2019
# https://leetcode.com/problems/palindrome-number/
# A Syahdeini
# Lame solution O(n*L) where L is the longest string in list(N)
class Solution:
    
    def match(self, str_a, str_b):
        for idx,char_a in enumerate(str_a):
            if (idx>(len(str_b)-1)):
                return str_b
            if char_a != str_b[idx]:
                return str_b[:idx]
        return str_a
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0: return ""
        prefix = strs[0]
        for _str in strs[1:]:
            prefix = self.match(prefix,_str)
        return prefix if prefix else ""
