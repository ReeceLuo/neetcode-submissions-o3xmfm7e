class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for value in tokens:
            if value.isnumeric() or (len(value) > 1 and value[0] == "-"):
                stack.append(int(value))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if value == "+":
                    stack.append(num1 + num2)
                elif value == "-":
                    stack.append(num1 - num2)
                elif value == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))

        return stack[0]