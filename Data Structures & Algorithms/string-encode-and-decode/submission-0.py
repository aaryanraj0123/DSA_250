class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Read the length number until '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Move j past '#'
            j += 1

            # Read exactly 'length' characters
            result.append(s[j:j + length])

            # Jump to the start of the next encoded string
            i = j + length

        return result
