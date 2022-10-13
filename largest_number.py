class largestNum(str):
  def __lt__(num1: str, num2: str) -> bool:
    return num1 + num2 > num2 + num1


class Solution:
  def largestNumber(self, nums: List[int]) -> str:

    return ''.join(sorted(map(str, nums), key=largestNum)).lstrip('0') or '0'
