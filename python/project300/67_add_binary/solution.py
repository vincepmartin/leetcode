class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Create a list to hold a and b in int form.
        aList = [0] * ((max(len(a), len(b)) - len(a))+1)
        bList = [0] * ((max(len(a), len(b)) - len(b))+1)

        for i in a:
            aList.append(int(i))

        for i in b:
            bList.append(int(i))

        # Store our answer.
        answer = [0] * len(bList)

     
 
        # Create our carry over bits.
        cList = [0] * (len(bList))
        for i in range(1, len(aList)):
            print(f'i: {i}')
            print(f'Carry bits: {aList[i]} & {bList[i]}')
            cList[i] = aList[i] & bList[i]

        # Shift.
        cList.append(0)
        cList.remove(0) 
        
        print(f'A: {aList}')
        print(f'B: {bList}') 
        print(f'C: {cList}')
        
        # Get our answer by xOR our bits.
        for i in range(len(cList)):
            answer[i] = aList[i] ^ bList[i] & cList[i]

        print(f'answer: {answer}')
        zerosAtBegin = 0
        for i in range(len(answer)):
            print(f'a[{i}] = {answer[i]}')
            if answer[i] == 0:
                zerosAtBegin += 1 
            else:
                break

        print(f'Answer: {answer}')


        return ''.join(map(str, answer[zerosAtBegin:]))
            



s = Solution()
# print(s.addBinary('1010', '11'))
print(s.addBinary('11', '1'))