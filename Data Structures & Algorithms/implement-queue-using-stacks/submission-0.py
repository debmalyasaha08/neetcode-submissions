class MyQueue:

    def __init__(self):
        # input stack handles all push operations
        self.input = []
        # output stack handles all pop and peek operations
        self.output = []

    def push(self, x: int) -> None:
        # Push element to the back of the queue
        self.input.append(x)

    def pop(self) -> int:
        # Move elements if output stack is empty, then return top element
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # If output stack is empty, pour all elements from input to output
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        # Return the top element of output stack
        return self.output[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks have no elements
        return not self.input and not self.output

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()