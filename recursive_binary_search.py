def recursive_bianry_search(list, target):
    """
    Recursive binary search will devide list into two halves and check if the middle element is equal to the target value.
    then repeat the process for the left of right into half until the target value is found or the list is empty.
    แบ่งครึ่งไปเรื่อยๆ จนกว่าจะเจอค่าที่ต้องการ หรือจนกว่ารายการจะว่างเปล่า

    recursive จะทำให้เข้าใจภาพตอน devided ได้ชัดกว่า แต่ว่า มีการเรียกตัวเองซ้ำใน function
    ทำให้ช้ากว่า iterative เพราะต้องมีการสร้าง new list ใหม่ทุกครั้งที่เรียก function
    """
    if len(list) == 0: #check if the list is empty
        return False # return None if the target value is not found
    else:
        midpoint = len(list) // 2 # find the middle index of the list

        if list[midpoint] == target: # check if the middle element is equal to the target value
            return True # return True if the target value is found
        else:
            if list[midpoint] < target: # check if the middle element is less than the target value
                return recursive_bianry_search(list[midpoint + 1:], target) # search in the right half of the list
            # [a:] --> เริ่มจาก a ไปถึงท้ายของ list
            else: # check if the middle element is greater than the target value
                return recursive_bianry_search(list[:midpoint], target) # search in the left half of the list


def verify(index):
    if index is not None:
        print("Target found at the Index: ",index)
    else:
        print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8]

result = recursive_bianry_search(numbers, 12)
verify(result)

result = recursive_bianry_search(numbers, 6)
verify(result)