def isOperand(symbol: str) -> bool:
  """ Check if symbol is digit

  :param (str) symbol: Symbol to check
  :returns (bool): True - if digit, False - if not digit
  """
  return True if symbol.isdigit() else False

def isLeftParenthesis(symbol: str) -> bool:
  """ Check if symbol is left parentathesis

  :param (str) symbol: Symbol to check
  :returns (bool): True - if left parentathesis, False - otherwise
  """
  return True if symbol == "(" else False

def isRightParenthesis(symbol: str) -> bool:
  return True if symbol == ")" else False

def hasLessOrEqualPriority(firstOperator: str, secondOperator: str) -> bool:
  """ Checks if first operator has less or equal priority compare to second operator.

  :param (str) firstOperator: First operator to compare
  :param (str) secondOperator: Second operator to compare
  :returns (bool): True - if less or equal priority, False - otherwise
  """
  priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,
    ')': 0
  }
  if priority.get(firstOperator) <= priority.get(secondOperator):
    return True;
  return False;