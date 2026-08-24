class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = []
        n = str(x)

        for i in n:
            number.append(i)
        #print(number)

        reverse_number = number[::-1]
        #print(reverse_number)

        if reverse_number == number:
            return True
        else:
            return False

test = Solution()
print(test.isPalindrome(121))