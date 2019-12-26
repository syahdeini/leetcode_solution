class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        head = 0
        tail = len(x)-1
        while head < tail:
            if x[head] == x[tail]:
                tail-=1
                head+=1
            else:
                break
        return True if head>=tail else False
