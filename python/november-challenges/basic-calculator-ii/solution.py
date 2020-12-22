from typing import List, Tuple

class Solution:
    def calculate(self, s: str) -> int:
        # We can use a stack to figure this out...
        numbers = []  
        operators = []

        # Parse the string into operators and numbers and place on our stack.
        self.getStacks(s, numbers, operators)

        # Print out the stacks for shits and giggles.
        print(numbers)
        print(operators)

        # We need to know what we should do first.  PEMDAS
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        } 

        # Pull things off the stack, do our calculations. 
        while len(numbers) > 1:
            a = numbers.pop()
            b = numbers.pop()

            if not numbers:
                nextNum = None
            else:
                nextNum = numbers[-1]
            
            op = operators.pop()

            if not operators:
                opNext = None
            else:
                opNext = operators[-1]

            if opNext == None or precedence.get(op) > precedence.get(opNext):
                numbers.append(self.doMath(b,a,op))
                # operators.append(op)
            
            else:
                numbers.pop()
                numbers.append(self.doMath(nextNum,b,opNext))
                operators.pop()
                operators.append(op)
                numbers.append(a)

        print(f'*** {numbers}')
        return numbers.pop()

    def getStacks(self, s: str, numbers: List[int], operators: List[str]) -> Tuple[List[int], List[str]]:
        tempNumber = []
        for c in s:
            if c == '+' or c == '-' or c == '*' or c == '/':
                # We have a number ready to add to our number stack.
                numbers.append(int(''.join(tempNumber)))
                tempNumber = []
                operators.append(c)

            else: 
                tempNumber.append(c)

        # Append out last number to our stack.
        numbers.append(int(''.join(tempNumber)))

    def doMath(self, a: int, b: int, op: str) -> int:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return 0
            else:
                return int(a/b)

        ''' 
        switcher = {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': int(a / b),
        }
        return switcher.get(op)
        '''

s = Solution()
print(s.calculate('0+0'))
            