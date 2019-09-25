class Solution:
    def defangIPaddr(self, address: str) -> str:
        out = ""

        for c in address:
            if c == ".":
                out += "[.]"
            else:
                out += c

        return out