""" linked_list.py
    ตัวอย่างการสร้าง linked list แบบง่าย ๆ
    โดยใช้ class Node และ class LinkedList
    เพิ่มความเข้าใจเกี่ยวกับ linked list และการทำงานงับ
"""
class Node:
    """
    Node ประกอบด้วย data และ pointer (next) ที่ชี้ไปยัง node ถัดไป
    ดังนั้นต้องสร้าง Object ของ Node ก่อนที่จะสร้าง linked list
    ต้องมี 2 attribute คือ data และ next
    อ่านเพิ่มกันลืมมมจ๊ะะ : https://www.geeksforgeeks.org/dsa/singly-linked-list-tutorial/
    """

    def __init__(self, data):
        self.data = data
        self.next = None   # ยังไม่ชี้ไปไหน (ตัวถัดไป)
        
    def __repr__(self):
        return "<Node data: %s>" % self.data # replace % with self.data

class LinkedList:
    def __init__(self):
        self.head = None   # จุดเริ่มต้น ชี้ไป node แรก

    def add(self, data):
        """ เพิ่ม node ใหม่ที่จุดท้ายของ linked list 
            takes O(n) time complexity
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:   # ไล่หา node สุดท้าย
            current = current.next
        current.next = new_node           # ต่อ node ใหม่เข้าไป


    """
    head -> node1 -> node2 -> node3 -> None
    ใส่ตัวแรกไปเช็คก่อนว่า ถ้า head เป็น None ให้ head ชี้ไป node ใหม่
    ถ้า head ไม่เป็น None ให้ไล่หา node สุดท้าย (current.next is not None) แล้วต่อ node ใหม่เข้าไป (current.next = new_node)
    1. สร้าง node ใหม่ (new_node = Node(data))
    """

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
        new_node.next = self.head # point new_node.next ไปที่ node แรก (self.head)
        self.head = new_node ## เปลี่ยน self.head ให้ชี้ไปที่ node ใหม่ (new_node)

    def search(self, key):
        """ ค้นหา node ที่มีค่า data เท่ากับ key
            takes O(n) time complexity
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else :
                current = current.next
        return None

    def delete(self, key):
        """ ลบ node ที่มีค่า data เท่ากับ key
            takes O(n) time complexity
        """
        current = self.head
        previous = None
        while current:
            if current.data == key:
                if previous is None:  # ลบ node แรก
                    self.head = current.next
                else:
                    previous.next = current.next
                return True  # ลบสำเร็จ
            previous = current
            current = current.next
        return False  # ไม่เจอ node ที่ต้องการลบ

    def insert(self, index, data):
        """ แทรก node ใหม่ที่ตำแหน่ง index
            takes O(n) time complexity
        """
        if index < 0:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.add_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        position = index

        while position > 1 and current is not None:
            current = current.next
            position -= 1

        if current is None:
            raise IndexError("Index out of bounds")

        new_node.next = current.next
        current.next = new_node