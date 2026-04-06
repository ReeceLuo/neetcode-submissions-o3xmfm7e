class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))
            encoded += "/"
            encoded += word
        return encoded

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != '/':
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            k = i + length
            output.append(s[i:k])
            i = k
        
        return output