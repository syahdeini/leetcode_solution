# 19.00 27-12-2019
# https://leetcode.com/problems/longest-common-prefix/
# A Syahdeini
# Runtime: 24 ms, faster than 98.52% o

# Most of the time we got fooled by our wrong intrepretation of the problem or our clumsiness of avoiding crucial information in the problem
# Such as this question, it is quite clear that the question state prefix which means, the same substring will always start from the first character. Therefore the solution can be much simpler.
class Solution:

    def compare(self, str1, str2):
        try:
            return str1.index(str2)
        except:
            return None

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        prefix = strs[0]
        for _str in strs[1:]:
            while self.compare(_str, prefix)!=0:
                prefix = prefix[:len(prefix)-1]
                if not prefix:
                    return ""
        return prefix
    
    
#Vertical scanning
class Solution:

    def compare(self, str1, str2):
        try:
            return str1.index(str2)
        except:
            return None

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        for idx, c in enumerate(strs[0]):
            for _str in strs[1:]:
                if idx==len(_str) or c!=_str[idx]:
                    return strs[0][:idx]
        return strs[0]
