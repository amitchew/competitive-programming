class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        begin = 0
        players = [i+1 for i in range(n)]


        while(len(players) > 1):
            next = (begin + k - 1) % n 
            players.pop(next)
            begin = next
            n -= 1

        return players[0]
