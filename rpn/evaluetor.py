def add(a: int, b:int) -> int:
    """ Add two numbers

    :param (int) a: First number
    :param (int) b: Second number
    :returns (int): Sum of two numbers
    """
    return a + b

def minus(a: int, b: int) -> int:
    """ Substruct b from a
    :param (int) a: left operand.
    :param (int) b: right operand
    :returns (int): Result of substruction
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """ Add two numbers

    :param (int) a: First number
    :param (int) b: Second number
    :returns (int): Sum of two numbers
    """
    return a * b

def division(a: int, b: int) -> int:
    """ Add two numbers

    :param (int) a: First number
    :param (int) b: Second number
    :returns (int): Sum of two numbers
    """
    return a / b

operators = {
        '+': add,
        '-': minus,
        '*': multiply,
        '/': division
}

def postixEval(stack: list) -> int:
    """ Evaluate postfix notation

    :param (list) stack: Stack with postfix notation
    :returns (int): Result of evaluation
    """
    res = list()
    for symbol in stack:
        if symbol.isdigit():
            res.append(int(symbol))
        elif not (res == []):
            b = res.pop()
            a = res.pop()
            temp = operators.get(symbol)(a, b)
            res.append(temp)
    return res.pop()

    

