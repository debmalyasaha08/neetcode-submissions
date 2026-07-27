class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for s in strs:
            encoded_strs += f"{len(s)}#{(s)}"
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1
            decode_list.append(s[i : i + length])
            i += length
        return decode_list 




