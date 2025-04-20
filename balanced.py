from class_Stack import Stack

def balanced(expression: str)->bool:
    stack = Stack()
    open_brackets = '([{'
    closed_brackets = ')]}'
    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for el in expression:
        if el in open_brackets:
            stack.push(el)
        elif el in closed_brackets:
            if stack.is_empty() or stack.pop() != matching_brackets[el]:
                return False
    return stack.is_empty()



