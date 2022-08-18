class Solution:
    def reverseWords(self, s: str) -> str:
        str_splt=s.split(" ") # space as a delimiter
        str_splt=[i[::-1] for i in str_splt] 
        return " ".join(str_splt)
