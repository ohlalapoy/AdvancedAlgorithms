class Solution:
    def isValid(self, s: str) -> bool:
        new_s = s.split()
        open = ("(","{","[") #position เปิด จะเป็น index เลขคี่เสมอ
        close = (")","}","]") #position ปิด จะเป้น index เลขคู่เสมอ

        sum_bracket01 = 0
        sum_bracket02 = 0
        sum_bracket03 = 0
        index01 = 0
        index02 = 0
        index03 = 0

        for index, string in enumerate(s): 
            if string == open[0] or string == close[0]:
                sum_bracket01 +=1
                index01 += index
            elif string == open[1] or string == close[1]:
                sum_bracket02 += 2
                index02 += index
            else:
                sum_bracket03 += 3
                index03 += index

        if index01  % 2 != 0 and sum_bracket01 == 2 :
            return True
        elif index02  % 2 != 0 and sum_bracket02 == 4:
            return True
        elif index03  % 2 != 0 and sum_bracket03 == 6:
            return True
        else: 
            return False

a = "([)]"
test = Solution()
print(test.isValid(a))