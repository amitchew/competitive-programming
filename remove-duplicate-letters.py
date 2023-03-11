class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter=Counter(s)

        stack=[]

        for items in s:
            while stack and counter[stack[-1]]>1 and items <stack[-1] and items not in stack:
                temp=stack.pop()
                counter[temp]-=1

            if items not in stack:
                stack.append(items)

            else:
                counter[items]-=1

        return("".join(stack))
