class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
Hash Map to solve this problem to optimize from O(n^2) to O(1)
วิธี hash map = เราเดินเข้าห้องแค่รอบเดียว แต่ถือสมุดจดติดตัว ทุกครั้งที่เจอคนใหม่ เราถามตัวเองว่า 
"ฉันต้องการคนอายุเท่าไหร่ถึงจะรวมกับคนนี้ได้ 30" (เช่นเจอคนอายุ 12 → เราต้องการคนอายุ 18) แล้วเปิดสมุดดูว่า
 เคยจดคนอายุ 18 ไว้รึยัง ถ้าเคยจด = เจอคู่แล้ว! ถ้ายังไม่เคย ก็จดคนอายุ 12 นี้ลงสมุดไว้ก่อน เดินหาคนต่อไป
"""
def two_sum_hashmap(nums, target):
    seen = {}  # สมุดจดที่เราถืออยู่
    
    for i, num in enumerate(nums):
        need = target - num       # "ฉันขาดอะไร"
        if need in seen:          # "ของที่ขาดเคยผ่านมาหรือยัง"
            return [seen[need], i]
        seen[num] = i             # จดคนนี้ไว้ก่อนเดินต่อ
    
    return []