class Solution:
    def freqAlphabets(self, s: str) -> str:
        # Let's make a hash map to hold our translations.
        t = {
            '1':'a',
            '2':'b',
            '3':'c',
            '4':'d',
            '5':'e',
            '6':'f',
            '7':'g',
            '8':'h',
            '9':'i',
            '10#': 'j',
            '11#': 'k',
            '12#': 'l',
            '13#': 'm',
            '14#': 'n',
            '15#': 'o',
            '16#': 'p',
            '17#': 'q',
            '18#': 'r',
            '19#': 's',
            '20#': 't',
            '21#': 'u',
            '22#': 'v',
            '23#': 'w',
            '24#': 'x',
            '25#': 'y',
            '26#': 'z',
        }    
        ans = []

        i = 0
        while i < len(s):
            # If we can look ahead 3 spaces.
            if i + 3 <= len(s) and s[i:i+3] in t:
                ans.append(t[s[i:i+3]])
                i+=3
            else:
                ans.append(t[s[i]])
                i+=1

        return ''.join(ans)

s = Solution()
print(s.freqAlphabets('10#11#12'))
print(s.freqAlphabets('1326#'))
print(s.freqAlphabets('12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#'))