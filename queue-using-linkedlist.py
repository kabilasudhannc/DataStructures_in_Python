from linked_list import Node, LinkedList


class Queue(LinkedList):
    def Enqueue(self, new_node):
        if self.isEmpty():
            self.first = new_node
            self.last = new_node

        else:
            current = self.last
            current.next = new_node
            self.last = new_node

    def Dequeue(self):
        if self.isEmpty():
            return -1

        else:
            current = self.first
            self.first = self.first.next
            return current

    def isFull(self):
        if self.first:
            return True

    def isEmpty(self):
        if not self.first:
            return True

    def __str__(self):
        if self.isEmpty():
            return 'Queue is empty.'

        else:
            queue = ['->[Front]']

            current = self.first
            while current:
                queue.insert(-1, f'->{current.value}')
                current = current.next
            queue.insert(0, '[Rear]')
            return ''.join(queue)


queue = Queue()

e1 = Node(4)
e2 = Node(5)
e3 = Node(6)

queue.Enqueue(e1)
queue.Enqueue(e2)
queue.Enqueue(e3)
# print(queue.Dequeue().value)
print(queue)
queue.reverse()
print(queue)
