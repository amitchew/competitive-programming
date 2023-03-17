class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        8
        1(pow)=1
        2(pow)=4
         8
        ---
        3(pow)=9
        4(pow)=16
        '''
        begin=0
        end=(x//2) +1 

        while begin<end:
            
            middle=begin+( end-begin +1)//2

            if middle*middle>x:
                end=middle-1

            else:
                begin=middle
            
        return begin

