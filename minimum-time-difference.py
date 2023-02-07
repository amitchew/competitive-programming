class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = float('inf')
        sortt = sorted(timePoints)
        time_len = len(sortt)
        for i in range(time_len-1):
            time = int(sortt[i].split(":")[0]) * 60 + int(sortt[i].split(":")[1]) 
            time_1 = time + (24*60)
            if i == 0:
                compare = sortt[i+1]
                c_s = int(compare.split(":")[0]) * 60 + int(compare.split(":")[1]) 
                compare_2 = sortt[-1]
                c_s2 = int(compare_2.split(":")[0]) * 60 + int(compare_2.split(":")[1])
                minutes = min(minutes,c_s-time,time_1-c_s,c_s2-time,time_1-c_s2 )
            else:
                compare = sortt[i+1]
                c_s = int(compare.split(":")[0]) * 60 + int(compare.split(":")[1]) 
                minutes = min(minutes,c_s-time,time_1-c_s)
        return minutes
