class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increments = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        if index > 0:
            self.increments[index - 1] += self.increments[index]  # Carry over the increment
        value = self.stack.pop() + self.increments[index]
        self.increments[index] = 0  # Reset increment for the popped value
        return value

    def increment(self, k: int, val: int) -> None:
        # Increment only the bottom k elements
        if k > len(self.stack):
            k = len(self.stack)
        if k > 0:
            self.increments[k - 1] += val  # Increment the (k-1)th index

# Example usage:
# obj = CustomStack(3)
# obj.push(1)
# obj.push(2)
# print(obj.pop())     # Returns 2
# obj.push(2)
# obj.push(3)
# obj.push(4)         # Stack remains [1, 2, 3]
# obj.increment(5, 100)  # Stack becomes [101, 102, 103]
# obj.increment(2, 100)  # Stack becomes [201, 202, 103]
# print(obj.pop())     # Returns 103
# print(obj.pop())     # Returns 202
# print(obj.pop())     # Returns 201
# print(obj.pop())     # Returns -1 (stack is empty)
