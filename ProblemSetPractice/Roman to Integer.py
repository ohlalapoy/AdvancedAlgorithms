class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I":1, "V":5,"X":10, "L":50,
            "C":100,"D":500,"M":1000
        }

        sum = 0
        #new_list = list(s)
        #print(new_list)
        for i in range(len(s)): # วนลูปตัวอักษรเข้าไปเช็ค 
            if i+1 < len(s) and symbol[s[i]] < symbol[s[i+1]]: 
        # ถ้า i+1 < len คือเช็คว่ามีตัวถัดไปไหม และ พอเอาตัวอักษรใร List ไปเทียบกับ dic ด้านบน Key น้อยกว่าตัวถัดไปไหม
        # ถ้าตัวหน้าดันค่าน้อยกว่าแล้วอยู่ข้างหน้า ก็ให้ลบออก เช่น XII X มากกว่า I จะไปตก else แต่บางเลข IX คือ 9 เลยต้องลบค่าออก
                sum -= symbol[s[i]]
            else: 
                sum += symbol[s[i]]
        return sum

s = "MCMXCIV"
test = Solution()
print(test.romanToInt(s))