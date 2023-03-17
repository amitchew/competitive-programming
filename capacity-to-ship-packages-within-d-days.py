class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        lower_bound=max(weights )
        upper_bound=sum(weights)

        answer=lower_bound
        def ship_carry(capacity):
            number_ships=1
            temp_capacity=capacity
            for weight in weights:
                if temp_capacity - weight<0:
                    number_ships+=1
                    temp_capacity=capacity

                temp_capacity=temp_capacity-weight

            if number_ships<=days :
                return True
            else:
                return False

        while lower_bound<=upper_bound:
            capacity=(lower_bound+upper_bound)//2

            if ship_carry(capacity):
                answer=capacity
                upper_bound=capacity-1
 
            else:
                lower_bound=capacity+1
        return answer








        
