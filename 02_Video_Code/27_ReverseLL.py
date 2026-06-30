class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Sll:
    def reverse(self,head):
        temp = self.head
        prev = None
        while temp.next is not None:
            front = temp.next 
            temp.next = prev
            prev = temp
            temp = front
        return prev