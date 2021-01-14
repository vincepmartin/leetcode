class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mtable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique = {}

        for word in words:
            temp = []
            for c in word:
                temp.append(mtable[ord(c) - 97])
            unique[''.join(temp)] = None

        return len(list(unique.keys()))
