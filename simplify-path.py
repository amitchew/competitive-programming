class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        '/home//
        /home

        "/../"
        /

        Input: path = "/home//foo/"
        Output: "/home/foo"

    '''
        stack=[]
        temp=0

        while temp<len(path):

            while temp<len(path) and path[temp]=='/':
                temp+=1

            begin=temp
            
            while temp<len(path) and path[temp]!='/':
                temp+=1
            
            temp_path=path[begin:temp]

            if temp_path=='..':
                if stack!=[]:
                    stack.pop()
            
            elif temp_path and temp_path!='.':
                stack.append(temp_path)

   

        if not stack:
            return '/'

        return '/'+'/'.join(stack)

        print(stack)


