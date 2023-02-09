class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        teams = len(skill)//2
        all = sum(skill)

        if all%teams != 0:
            return -1

        skill.sort()
        l=0
        r=len(skill)-1
        team_chemistry=0

        summ=0

        while l<r:
            if(skill[l]+skill[r])!=summ and l>0:
                return -1
            team_chemistry+= (skill[l]*skill[r])
            summ= (skill[l]+skill[r])
            l+=1
            r-=1
        return team_chemistry

            
