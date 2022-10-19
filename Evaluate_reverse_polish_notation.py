class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    num_list = []
    operator = {
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y),
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
    }

    for items in tokens:
      if items in operator:
        y = num_list.pop()
        x = num_list.pop()
        num_list.append(operator[items](x, y))
      else:
        num_list.append(int(items))

    return num_list[0]
