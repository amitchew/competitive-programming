class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken=0

        while(tickets[-1]!=0):
            time_taken+=1

            if(tickets[0]==1):
                tickets.pop(0)

                if(k==0):
                    return time_taken
                else:
                    k-=1
            
            else:
                tickets.append(tickets[0]-1)

                tickets.pop(0)

                if (k==0):
                    k=int(len(tickets))-1

                else:
                    k-=1
