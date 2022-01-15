class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_str = list(s.strip().split())
        reverse_str = " ".join(reverse_str[::-1])
        return reverse_str