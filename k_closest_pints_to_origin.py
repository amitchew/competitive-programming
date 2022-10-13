class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    def Distance(point: List[int]) -> int:
      return point[0] * point[0] + point[1] * point[1]

    def pick(l: int, r: int, x: int) -> None:
      current = points[r]

      next = l
      for i in range(l, r):
        if Distance(points[i]) <= Distance(current):
          points[next], points[i] = points[i], points[next]
          next += 1
      points[next], points[r] = points[r], points[next]

      count = next - l + 1  
      if count == x:
        return
      if count > x:
        pick(l, next - 1, x)
      else:
        pick(next + 1, r, x - count)

    pick(0, len(points) - 1, K)
    return points[0:K]
