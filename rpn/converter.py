from .helpers import isOperand
from .helpers import isLeftParenthesis
from .helpers import isRightParenthesis
from .helpers import hasLessOrEqualPriority

def toPostfix(infix: str) -> list:
  """ Converts infix to postfix notation.

  :param (str) infix: Infix string
  :returns (list): List of postfix notation
  """
  stack = []
  postfix = []

  for c in infix:
      if isOperand(c):
          postfix.append(c)
      else:
          if isLeftParenthesis(c):
              stack.append(c)
          elif isRightParenthesis(c):
              operator = stack.pop()
              while not isLeftParenthesis(operator):
                  postfix.append(operator)
                  operator = stack.pop()              
          else:
              while (not (stack == [])) and hasLessOrEqualPriority(c,stack[-1]):
                  postfix.append(stack.pop())
              stack.append(c)

  while (not (stack == [])):
      postfix.append(stack.pop())
  return postfix