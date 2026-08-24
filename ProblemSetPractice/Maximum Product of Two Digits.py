class Solution:
    def maxProduct(self, n: int) -> int:
        self.n = n

        split_num = str(n)
        new_num = []
        sum_two_digit = []
        #for i in range(len(split_num)):
        for num in split_num:
            new_num.append(num)

        for i in range(0,len(new_num)):
            for j in range(i+1,len(new_num)):
                sum = int(new_num[i])*int(new_num[j])
                sum_two_digit.append(sum)
        return(max(sum_two_digit))
