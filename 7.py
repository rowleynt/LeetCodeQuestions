class Solution:
    def reverse(self, x: int) -> int:
        d_lst = [char for char in str(abs(x))]
        d_lst.reverse()
        digits = ''.join(d_lst)
        digits = digits.rstrip("0") if len(digits) > 1 else digits
        if int(digits) < (2**31 - 1):
            return int(digits) if x >= 0 else 0 - int(digits)
        else:
            return 0