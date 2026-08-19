""" linked_list.py
    ตัวอย่างการสร้าง linked list แบบง่าย ๆ
    โดยใช้ class Node และ class LinkedList
    เพิ่มความเข้าใจเกี่ยวกับ linked list และการทำงานงับ
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # ยังไม่ชี้ไปไหน

class LinkedList:
    def __init__(self):
        self.head = None   # จุดเริ่มต้น ชี้ไป node แรก

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:   # ไล่หา node สุดท้าย
            current = current.next
        current.next = new_node           # ต่อ node ใหม่เข้าไป

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def add_at_beginning(self, data):
        """ เพิ่ม node ใหม่ที่จุดเริ่มต้นของ linked list 
            takes O(1) time complexity
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node