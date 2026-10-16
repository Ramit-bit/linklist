class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def add_last(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def add_middle(self, data, pos):
        new = Node(data)
        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        new.next = temp.next
        temp.next = new

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_middle(self, pos):
        if self.head is None:
            return
        if pos == 1:
            self.delete_first()
            return
        temp = self.head
        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp.next is None:
            print("Invalid position")
            return
        temp.next = temp.next.next

    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(count)
        return


l = LinkedList()

print("Enter 7 nodes:")
for i in range(7):
    l.add_last(input())

print("Original linked list:")
l.display()

l.add_first(9)
print("After adding at first:")
l.display()

l.add_last(0)
print("After adding at last:")
l.display()

l.add_middle(30, 4)
print("After adding at middle (position 4):")
l.display()

l.delete_first()
print("After deleting first:")
l.display()

l.delete_last()
print("After deleting last:")
l.display()

l.delete_middle(4)
print("After deleting middle (position 4):")
l.display()

l.reverse()
print("After reversing:")
l.display() 
l.length()