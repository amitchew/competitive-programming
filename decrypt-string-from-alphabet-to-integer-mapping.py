class Solution:
  def freqAlphabets(self, s: str) -> str:
    item = 0
    result = ''

    while item < len(s):
      if item + 2 < len(s) and s[item + 2] == '#':
        result += chr(int(s[item:item + 2]) + ord('a') - 1)
        item += 3
      else:
        result += chr(int(s[item]) + ord('a') - 1)
        item += 1

    return result
