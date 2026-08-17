"""
 Binary search will devide list into two halves and check if the middle element is equal to the target value.
 then repeat the process for the left of right into half until the target value is found or the list is empty.
 แบ่งครึ่งไปเรื่อยๆ จนกว่าจะเจอค่าที่ต้องการ หรือจนกว่ารายการจะว่างเปล่า

 binary search จะต้องถูก sort ก่อนเสมอ ก่อนนำมาใช้ในการค้นหา เพราะ binary search 
 จะทำการแบ่งครึ่งของ list และตรวจสอบค่ากลางของ list ว่าตรงกับ target หรือเปล่า
"""

def binary_search(list, target):
    first = 0 # to start from the first index of the list
    last = len(list) - 1 # to start from the last index of the list

    while first <= last: # loop until the first index is less than or equal to the last index
        midpoint = (first + last) // 2 # find the middle index of the list
    
        if list[midpoint] == target: # check if the middle element is equal to the target value
            return midpoint # return the index of the target value
        elif list[midpoint] < target: # check if the middle element is less than the target value
            first = midpoint + 1 # search in the right half of the list คือเริ่ม first จาก midpoint + 1
        else: # check if the middle element is greater than the target value
            last = midpoint - 1 # search in the left half of the list
    return None # return None if the target value is not found

"""
Trick ในการทำลองคิอดเป็นลำดับขั้นตอนด จะทำโจทยืง่ายขึ้นมากๆ 
เหมือนเราลงมือทำเอง แค่เราต้องคิดเป็นขั้นตอนดีกว่า และสั่งให้คอมพิวเตอร์ทำตามขั้นตอนที่เราคิดไว้
"""
def verify(index):
    if index is not None:
        print("Target found at the Index: ",index)
    else:
        print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
