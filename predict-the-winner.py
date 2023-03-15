class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        result = [0, 0, 0]

        def winner(nums: List[int], result) -> bool:
            if len(nums) == 0:
                return result[0] >= result[1]

            if len(nums) == 1:
                if result[2] == 0:
                    return result[0] + nums[0] >= result[1]
                else:
                    return result[0] >= result[1] + nums[0]


            if result[2] == 0:
                return winner(nums[1:], [result[0] + nums[0], result[1], 1]) or winner(nums[:-1], [result[0] + nums[-1], result[1], 1])
           
           
            else:
                return winner(nums[1:], [result[0], result[1] + nums[0], 0]) and winner(nums[:-1], [result[0], result[1] + nums[-1], 0])
            return result
        
        
        return winner(nums, result)
