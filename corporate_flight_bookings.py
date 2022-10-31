class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total_seats=[]
        for(start,end,seats) in bookings:
            total_seats.append((start-1,seats))
            total_seats.append((end+1-1, -seats))
        total_seats.sort()
        results = [0] *n
        for event in total_seats:
            if event[0]>=n:
                continue
            results[event[0]]+=event[1]
        for i in range(1,n):
            results[i] += results[i-1]
        return results
