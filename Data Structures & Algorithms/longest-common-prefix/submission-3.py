class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            # Check every other string in the list
            for s in strs:
                # If current index 'i' is out of bounds for string 's'
                # OR if the character at index 'i' doesn't match
                if i == len(s) or s[i] != strs[0][i]:
                    # Return the prefix found so far
                    return res
            res += strs[0][i]
        return res

      
        

     

               
         

                