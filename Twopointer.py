'''
Two pointers has 2 ways to solve
- Same direction : starter and end start from the first index and secound index representively
- opposite : starter started from first index and the secound one start from the end

Two Pointer เป็นเทคนิคที่ใช้ pointer สองตัววิ่งไล่ตามอาร์เรย์ (หรือ list) เพื่อลด time complexity จาก O(n²) เหลือ O(n)
Trick ง่ายๆคือ ถ้าโจทย์ต้องการหาคู่ หรือ ต้องเทียบ pair ของมันลองใช้ TwoPointer ดูก่อน 

type of problem that you usually use Twopointer to solve
- Palindromes
- Reversals
- Merging sorted data
- "K" sized comparisons

'''
#Two Sum - Sorted Array

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1   # ต้องการค่ามากขึ้น เลื่อน left ไปทางขวา
        else:
            right -= 1  # ต้องการค่าน้อยลง เลื่อน right มาทางซ้าย
    
    return None  # ไม่พบคู่ที่ตรงกัน

# ตัวอย่างการใช้งาน
arr = [2, 7, 11, 15, 20]
target = 22
print(two_sum_sorted(arr, target))  # ผลลัพธ์: [1, 3] -> 7+15=22


#Palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

#Sorted Array (Fast-Slow Pointer)
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0  # ตำแหน่งสุดท้ายของค่าที่ไม่ซ้ำ
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1  # จำนวนค่าที่ไม่ซ้ำ

arr = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(arr)
print(arr[:new_length])  # [1, 2, 3, 4, 5]

#Container With Most Water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)
        
        # เลื่อน pointer ที่มีความสูงน้อยกว่า
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(heights))  # 49