class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop() #a is right and b is left in stack.pop()
                stack.append(b - a)  #left - right
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) #in python int rounds towards 0 
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
        return stack[0]