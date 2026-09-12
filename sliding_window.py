'''
Dynamic Window's problem
- Find the length of the substring with atr most K unique charaters
- what's the smallest subarray with sum greater than target
- Return the logest window where a certain rule is valid
- Find the largest sum in the list

'''

#Template

def sliding_window_fixed(input,window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans,window)
    return ans

#Fixed Size Window - หาผลรวมสูงสุดของ subarray ขนาด k
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None
    
    # คำนวณผลรวมของ window แรก
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # เลื่อน window ไปทีละ 1 ตำแหน่ง
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # เพิ่มตัวใหม่ ลบตัวเก่า
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# ตัวอย่างการใช้งาน
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # ผลลัพธ์: 9 (5+1+3)

# หา subarray สั้นที่สุดที่ผลรวม >= target
def min_subarray_len(target, arr):
    n = len(arr)
    left = 0
    window_sum = 0
    min_len = float('inf')
    
    for right in range(n):
        window_sum += arr[right]
        
        # หด window จากซ้ายเมื่อผลรวมมากพอแล้ว
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# ตัวอย่างการใช้งาน
arr = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len(target, arr))  # ผลลัพธ์: 2 ([4,3])

#Sliding Window ร่วมกับ Hash Map - หา substring ยาวที่สุดที่ไม่มีตัวอักษรซ้ำ
def length_of_longest_substring(s):
    char_index = {}  # เก็บตำแหน่งล่าสุดของแต่ละตัวอักษร
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char = s[right]
        
        # ถ้าตัวอักษรนี้เคยเจอ และอยู่ใน window ปัจจุบัน
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# ตัวอย่างการใช้งาน
s = "abcabcbb"
print(length_of_longest_substring(s))  # ผลลัพธ์: 3 ("abc")