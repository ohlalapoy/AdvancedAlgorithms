class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I":1, "V":5,"X":10, "L":50,
            "C":100,"D":500,"M":1000
        }

        sum = 0
        #new_list = list(s)
        #print(new_list)
        for i in range(len(s)): # i in new_list
            if i+1 < len(s) and symbol[s[i]] < symbol[s[i+1]]: #pass string เข้ามา
                sum -= symbol[s[i]]
            else: 
                sum += symbol[s[i]]
        return sum

s = "MCMXCIV"
test = Solution()
print(test.romanToInt(s))