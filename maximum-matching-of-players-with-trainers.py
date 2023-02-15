class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        answer, left, right = 0, 0, 0
    
        while left < len(players) and right < len(trainers):

            if players[left] <= trainers[right]:
                left += 1
                answer += 1
            
            right += 1

        return answer
