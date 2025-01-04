class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for item in tokens:
            if item not in '+-/*':
                stack.append(int(item))
            else:
                m, n = stack.pop(), stack.pop()
                if item == '+':
                    o = n + m
                elif item == '-':
                    o = n - m
                elif item == '*':
                    o = n * m
                else:
                    o = int(n / m)
            
                stack.append(o)
            
        return stack.pop()
