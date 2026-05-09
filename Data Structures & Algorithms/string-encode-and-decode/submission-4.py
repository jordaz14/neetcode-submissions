class Solution:

    def encode(self, strs: List[str]) -> str:
        signature = ""
        for string in strs:
            signature += str(len(string)) + "."
        
        signature += str(len(signature))
        encoded_string = "".join(strs) + signature
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        signature_length = int(s.split(".")[-1])
        signature_length += len(str(signature_length))
        signature = s[-signature_length:].split(".")[:-1]

        ans = []
        ptr = 0
        
        for word in signature:
            sub_string = ""
            for i in range(int(word)):
                sub_string += s[ptr]
                ptr += 1
            ans.append(sub_string)

        return ans

        