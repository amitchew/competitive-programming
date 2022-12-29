class Solution:
  def appendCharacters(self, s: str, t: str) -> int:
    i = 0  
    for x in s:
      if x == t[i]:
        i += 1
        if i == len(t):
          return 0

    return len(t) - i
