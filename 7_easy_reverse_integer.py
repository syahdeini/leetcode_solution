#26-12-2019
#https://leetcode.com/problems/reverse-integer/
# A Syahdeini.

import math

class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        if len(a)==1:
            return a
        sign = ''
        if a[0]=='-':
            sign = '-'
            a = a[1:]
        idx=0
        
        a = a[::-1]
        
        max_threshold = 2**31 -1
        min_threshold = 2**31 * -1
        
        if int(a)<min_threshold or int(a)>max_threshold:
            return 0
        
        while a[idx]=='0':
            a = a[idx+1:]
        return sign+a
