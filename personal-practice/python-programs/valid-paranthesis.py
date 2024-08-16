def valid_paranthesis(paranthesis):
    stack = []
    pairs = {'(':')', '[':']', '{':'}'}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif len(stack) == 0 or char!= pairs[stack.pop()]:
            return False
    return len(stack) == 0


strings = ["()", "()[]{}", "(]"]
for s in strings:
    print(valid_paranthesis(s))