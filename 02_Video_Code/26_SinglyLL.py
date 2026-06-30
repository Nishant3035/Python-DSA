class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class SinglyLL:
    def __init__(self):
        self.head = None
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
    def traverse(self):
        if self.head == None:
            print("Sll is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value,end = " ")
                curr = curr.next
            print()
    def insert(self,value,position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count < position:
                prev_node = curr
                curr = curr.next
                count+=1
            prev_node.next = new_node
            new_node.next = curr
    def delete(self,value):
        temp = self.head
        if temp.next is not None:
            if temp.value == value:
                self.head = temp.next
                return
            else:
                found = False
                prev_node = None
                while temp is not None:
                    if temp.value == value:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev_node.next = temp.next
                    return
                else:
                    print("Node not found")


        

sll = SinglyLL()
sll.append(10)
sll.traverse()