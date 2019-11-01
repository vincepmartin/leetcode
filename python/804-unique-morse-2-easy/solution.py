from typing import List

class Solution:
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        translatedWords = set() 

        for word in words:
            translatedWord = [] 
            for letter in word: 
                translatedWord.append(transTable[ord(letter) - ord('a')])
            translatedWords.add(''.join(translatedWord))

        return len(translatedWords)

s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))