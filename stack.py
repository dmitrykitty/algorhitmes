def evalRPN(tokens: List[str]) -> int:
    stack = []
    for c in tokens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '-':
            n1, n2 = stack.pop(), stack.pop()
            stack.append(n2 - n1)
        elif c == '/':
            n1, n2 = stack.pop(), stack.pop()
            stack.append(int(n2 / n1))
        else:
            stack.append(int(c))

    return stack[0]


def isValid(s: str) -> bool:
    pair = {'(': ')', '[': ']', '{': '}'}
    stack_ar = []

    for brack in s:
        if brack in pair:
            stack_ar.append(brack)
        else:
            if not stack_ar:
                return False
            prev = stack_ar.pop()

            if brack != pair[prev]:
                return False

    return len(stack_ar) == 0
