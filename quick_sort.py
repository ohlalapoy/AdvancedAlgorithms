import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# Best Case
def quicksort(values):
    if values < 1:
        return values

'''
"แบ่งแล้วเรียง" (divide and conquer) โดยเลือกตัวเลขตัวหนึ่งมาเป็น "ตัวหลัก" (pivot) แล้วแบ่งข้อมูลที่เหลือออกเป็น 2 กลุ่ม: กลุ่มที่น้อยกว่า pivot กับกลุ่มที่มากกว่า pivot จากนั้นก็ทำแบบเดียวกันซ้ำๆ กับแต่ละกลุ่มย่อย จนกว่าทุกอย่างจะเรียงลำดับเสร็จ
หลักการทำงาน (แบบง่ายที่สุด)
เลือก pivot — เลือกค่าใดค่าหนึ่งในลิสต์มาเป็นตัวหลัก (มักเลือกตัวสุดท้ายหรือตัวแรก)
แบ่งกลุ่ม (partition) — เทียบทุกตัวในลิสต์กับ pivot: ตัวที่น้อยกว่าไปอยู่ฝั่งซ้าย ตัวที่มากกว่าไปอยู่ฝั่งขวา
ทำซ้ำ (recursive) — เอาหลักการเดียวกันนี้ไปใช้กับฝั่งซ้ายและฝั่งขวาต่อ จนกว่าแต่ละกลุ่มจะเหลือ 0-1 ตัว (เรียงเสร็จโดยอัตโนมัติ)
รวมกลับ — เอาฝั่งซ้าย (เรียงแล้ว) + pivot + ฝั่งขวา (เรียงแล้ว) มาต่อกัน ก็จะได้ลิสต์ที่เรียงสมบูรณ์
'''
# The Quicksort algorithm relies on recursion. To implement it, we'll
# write a recursive function. We'll accept the list of numbers to
# sort as a parameter.
def quicksort(values):
  # Quicksort is recursive because it keeps calling itself with
  # smaller and smaller subsets of the list you're trying to
  # sort. We're going to need a base case where the recursion stops,
  # so it doesn't enter an infinite loop.  Lists that are empty don't
  # need to be sorted. And lists with just one element don't need to
  # be sorted, either. In both cases, there's nothing to flip
  # around. So we'll make that our base case; if there are 0 or 1
  # elements in the list passed to the "quicksort" function, we'll
  # return the unaltered list to the caller.
  if len(values) <= 1:
    return values
  # The code from here on out represents the recursive case.  We need
  # to create a list that will hold all the values less than the
  # pivot. That list will be empty at first.
  less_than_pivot = []
  # We do the same for values greater than the pivot.
  greater_than_pivot = []
  # Next we need to choose the pivot value. For now, we just grab the
  # first item from the list.
  pivot = values[0]
  # Then we loop through all the items in the list following the pivot.
  for value in values[1:]:
    # We check to see whether the current value is less than or equal
    # to the pivot.
    if value <= pivot:
      # If it is, we copy it to the sub-list of values less than the
      # pivot.
      less_than_pivot.append(value)
    # Otherwise, the current value must be greater than the pivot...
    else:
      # So we copy it to the other list.
      greater_than_pivot.append(value)
  # This last line is where the recursive magic happens. We call
  # quicksort recursively on the sub-list that's less than the
  # pivot. We do the same for the sub-list that's greater than the
  # pivot. Those two calls will return sorted lists, so we combine
  # the sorted values less than the pivot, the pivot itself, and the
  # sorted values greater than the pivot. That gives us a complete,
  # sorted list, which we return.
  print("%15s %1s %-15s" % (less_than_pivot,pivot,greater_than_pivot)) # ให้เห็นภาพตอน compare pivot แล้วย้ายฝั่งไปมาก่อน merge
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Lastly, we need to call our quicksort function with our list of
# numbers, and print the list it returns.
sorted_numbers = quicksort(numbers)
print(sorted_numbers)