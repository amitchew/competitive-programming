class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses={}

        for win,loser in matches:
            losses[win]=losses.get(win,0)
            losses[loser]=losses.get(loser,0)+1
        
        winn=[]
        one_loose=[]
        
        for team ,loose in losses.items():
            if loose==0:
                winn.append(team)
            elif loose==1:
                one_loose.append(team)

        return (sorted(list(winn)),sorted(list(one_loose)))
