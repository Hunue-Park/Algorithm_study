class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in range(len(s)):
            char = s[i]
            stack.append(char)
        goal = []    
        for i in range(len(s)):
            rev_char = stack.pop()
            goal.append(rev_char)
        
        print(rev_char)
    