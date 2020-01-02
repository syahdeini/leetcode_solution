# 22:42 02-01-2020
# https://leetcode.com/problems/valid-parentheses/
# Runtime: 32 ms, faster than 60.38% of Python3 online submissions for Valid Parentheses.
# A Syahdeini


class stack:
    # First in, last out
    def __init__(self):
        self._stack = []
      
    @property
    def stack(self):
        return self._stack
    
    def last(self):
        if len(self._stack) > 0:
            return self._stack[-1]
        return None
    
    @stack.getter
    def stack(self):
        if len(self._stack) > 0:
            val = self._stack[-1]
            del self._stack[-1]
            return val
        return []
    
    @stack.setter
    def stack(self, val):
        self._stack.append(val)
    
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack_obj = stack()
        for _char in s:
            if _char in ["(","{","["]:
                stack_obj.stack = _char
            else:
                last = stack_obj.stack
                if _char == ')' and last == '(':
                    continue
                elif _char == '}' and  last == '{':
                    continue
                elif _char == ']' and last == '[':
                    continue
                else:
                    return False
        if len(stack_obj.stack) > 0:
            return False
        return True
