from os import close
from numpy import append


string = "{(({[())]}))}"

def valid_parenthesis(string):
    stack = []
    close_open = {')':'(',']':'[','}':'{'}

    for ch in string:
        if stack and ch in close_open:
            if stack[-1] == close_open[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return not stack

ans = valid_parenthesis(string)
print(ans)
