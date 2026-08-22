class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < reslen:
                    res, reslen = [l, r], r - l + 1
                left_char = s[l]
                window[left_char] -= 1
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                l += 1
        start, end = res
        return s[start:end + 1] if reslen != float("inf") else ""


            