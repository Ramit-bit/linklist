class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = new
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new.next = self.head
        temp.next = new
        self.head = new

    def add_last(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = new
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new
        new.next = self.head

    def add_middle(self, data, pos):
        if pos == 1:
            self.add_first(data)
            return
        temp = self.head
        for i in range(pos - 2):
            if temp.next == self.head:
                print("Invalid position")
                return
            temp = temp.next
        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete_first(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def delete_middle(self, pos):
        if self.head is None:
            return
        if pos == 1:
            self.delete_first()
            return
        temp = self.head
        for i in range(pos - 2):
            if temp.next == self.head:
                print("Invalid position")
                return
            temp = temp.next
        if temp.next == self.head:
            print("Invalid position")
            return
        temp.next = temp.next.next

    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return
        prev = None
        curr = self.head
        while True:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            if curr == self.head:
                break
        self.head.next = prev
        self.head = prev

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        


cll = CircularLinkedList()

print("Enter 7 nodes:")
for i in range(7):
    cll.add_last(int(input()))

print("Original circular linked list:")
cll.display()
print("\n")
cll.add_first(90)

cll.display()
print("added at the first\n")
cll.add_last(8)

cll.display()
print("added at the last\n")
cll.add_middle(60, 5)

cll.display()
print("added in the middle\n")
cll.delete_first()

cll.display()
print("deleted the first\n")
cll.delete_last()

cll.display()
print("deleted the last\n")
cll.delete_middle(3)

cll.display()
print("deleted from the middle\n")
cll.reverse()

cll.display()
print("reversed the list\n")