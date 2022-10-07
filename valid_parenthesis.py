class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for parentheses in s:
            if parentheses == '(':
                stack.append(')')
            elif parentheses =='{':
                stack.append('}')
            elif parentheses =='[':
                stack.append(']')
            elif not stack or stack.pop() !=parentheses:
                return False
        return not stack
