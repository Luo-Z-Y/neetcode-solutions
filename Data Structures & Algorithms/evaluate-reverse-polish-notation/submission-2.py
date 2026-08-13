class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for token in tokens:
            if token == "+":
                first_num = num_stack.pop()
                second_num = num_stack.pop()
                num_stack.append(first_num + second_num)
            elif token == "*":
                first_num = num_stack.pop()
                second_num = num_stack.pop()
                num_stack.append(first_num * second_num)
            elif token == "-":
                first_num = num_stack.pop()
                second_num = num_stack.pop()
                num_stack.append(second_num - first_num)
            elif token == "/":
                first_num = num_stack.pop()
                second_num = num_stack.pop()
                num_stack.append(int(second_num / first_num))
            else:
                num_stack.append(int(token))
        
        return num_stack[0]
