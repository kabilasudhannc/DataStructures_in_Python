class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
        self.size = 0

    def addFirst(self, new_node):
        current = self.first
        if self.first:
            new_node.next = current
            self.first = new_node

        else:
            self.first = new_node
            self.last = new_node
        self.size += 1

    def addLast(self, new_node):
        current = self.last
        current.next = new_node
        self.last = new_node
        self.size += 1

    def deleteFirst(self):
        if self.first:
            self.first = self.first.next
            self.size -= 1

    def deleteLast(self):
        current = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        if self.first:
            while current:
                if current.next == self.last:
                    self.last = current
                    self.last.next = None
                current = current.next
        self.size -= 1
        return -1

    def __str__(self):
        if not self.first:
            return

        current = self.first
        values = '[Head] -> '
        if self.first:
            while current:
                values += f'[{current.value}] -> '
                current = current.next
            values += '[Last]'
            return values
        else:
            return -1

    def indexOf(self, value):
        current = self.first
        count = 0
        if self.first:
            while current:
                if current.value == value:
                    return count
                current = current.next
                count += 1
            else:
                return -1
        else:
            return -1

    def sizeof(self):
        return self.size

    def reverse(self):
        previous = self.first
        current = self.first.next

        if self.first:
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            self.last = self.first
            self.last.next = None
            self.first = previous

        else:
            return -1

    def getKthFromTheEnd(self, k):
        if not self.first:
            return 'List is empty'

        a = self.first
        b = self.first
        for i in range(k - 1):
            b = b.next

        if not b:
            raise ValueError('K is grater than the size of the list')

        while b != self.last:
            a = a.next
            b = b.next

        return a.value


e1 = Node(4)
e2 = Node(2)
e3 = Node(3)
e4 = Node(6)
e5 = Node(7)

# ll = LinkedList()
# ll.addFirst(e1)
# ll.addLast(e2)
# ll.addLast(e3)
# ll.addLast(e4)
# ll.deleteLast()
# ll.deleteFirst()
# ll.addFirst(e5)
# print(ll.indexOf(8))
# print(ll)
# print(ll.sizeof())
# ll.reverse()
# print(ll)
# print(ll.getKthFromTheEnd(4))
