# valid parentheses

# type s: str
# return type: bool
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        for i in s:
            if i not in table: 
                stack.append(i)  
            elif not stack or table[i] != stack.pop():
                return False
        return len(stack) == 0 
        # 마지막 리턴에서 len(stack) == 0 인것까지 동시에 확인할 수 있는
        # true, false 값.
