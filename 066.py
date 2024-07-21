class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 0
        i = len(digits)-1
        carry = 0
        while carry!=0 or i == len(digits)-1:
            if i < 0:
                digits.insert(0, carry)
            else:
                x = digits[i] + carry + (1 if i == len(digits)-1 else 0)
                digits[i] = x%10

            carry = (int)(x/10)
            x = x%10

            i -= 1

        return digits
