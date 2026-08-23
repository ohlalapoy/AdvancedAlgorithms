from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorted a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatly merge the sublists to produce sorted sublists until one remains
    
    Returns a sorted linked list
    """
l = LinkedList()
l.add(2)
print(l)