def merge_sort(list):
    """
    Sort a list in ascending order 
    Return a new sorted list

    Devide: Find the middle of the list and devide into sublists
    conquer: Resursively sort the sublists created in previous step
    Combine: Merge the sorted sublists create the previous step
    Takes O(n log n)
    """

    if len(list) <= 1: # to stop when we got the value
        return list

    left_half, right_half = split(list) #Devide from this step
    left = merge_sort(left_half) #merge from this step
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    '''
    Divide the sorted list at the midpoint into sublists
    Return two sublists - left and right
    Takes O(k log n) ---> depends on size of data we have to split
    '''
    mid = len(list)//2
    left = list[:mid] #start list from the beginning to mid
    right = list[mid:] # start list from mid to end 

    return left, right

def merge(left,right):
    '''
    Merge two lists(arrays), sorting them in the process
    Returns a new merged list
    Takes O(n)
    '''
    l = [] #list เปล่าเพื่อรอเก็บค่าที่เรียงแล้วเข้ามา
    i = 0 #position ของตัวแปลใน list 
    j = 0

    """
    แต่เงื่อนไขนี้ต้องระวังเพราะถ้าเกิดเจอเคส len ของฝั่งใดฝั่งหนนึ่งน้อยกว่า มันจะ return False 
     และออกจาก loop ทำให้ตัวถัดๆไปไม่ได้ถูก sort
     เราเลยต้องสร้าง while loopอีกรอบข้างล่างเพื่อเก็บตกตัวที่เหลือในกรณี
     while แรกเราใช้ไม่ได้ 
    """
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            l.append(left[i])
            i +=1 # increase 1 to proces nezt reound
        else: 
            l.append(right[j])
            j+=1

    while  i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

#alist = [54,62,93,17,77,31,44,55,20]
#l = merge_sort(alist)
#print(l)

def verify_sorted(list):
    n = len(list)

    if n == 0 or n ==1:
        return True
    return list[0] < list[l] and verify_sorted(list[1:])