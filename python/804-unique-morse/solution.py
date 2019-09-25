class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morseTranslations = set()

        for word in words:
            morseTranslations.add(self.wordToMorse(word))

        return len(morseTranslations)

    def wordToMorse(self, word):
        morseConvert = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = []

        for c in word:
            # I think this can be slow...
            # morse += morseConvert[ord(c) - 97]
            morse.append(morseConvert[ord(c) - 97])
        return ''.join(morse)

s = Solution()
t1 = ["gin", "zen", "gig", "msg"]

print(s.uniqueMorseRepresentations(t1))