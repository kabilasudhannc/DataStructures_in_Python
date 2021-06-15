from linked_list import LinkedList, Node


class Stack(LinkedList):
    def push(self, new_node):
        top = self.first
        if not self.first:
            self.first = new_node

        if self.first:
            new_node.next = top
            self.first = new_node

    def pop(self):
        if not self.first:
            return -1

        if self.first:
            current = self.first
            self.first = self.first.next
            return current

    def peek(self):
        if not self.first:
            return -1

        if self.first:
            top = self.first
            return top

    def isBalanced(self, expression):
        for char in expression:
            if char == '(' or char == '{' or char == '[' or char == '<':
                node = Node(char)
                self.push(node)

            if not self.first:
                return False

            elif (char == ')' and self.first.value == '(' or
                  char == '}' and self.first.value == '{' or
                  char == ']' and self.first.value == '[' or
                  char == '>' and self.first.value == '<') and self.first is not Node:
                return True

        return False


# e1 = Node(3)
# e2 = Node(2)
# e3 = Node(4)
# e4 = Node(5)
#
stack = Stack()
#
# stack.push(e1)
# stack.push(e2)
# print(stack.peek().value)
# stack.pop()
# print(stack.peek().value)

string = 'Hello World!'
for char in string:
    node = Node(char)
    stack.push(node)

reverse_string = ''
for i in range(len(string)):
    char = stack.pop()
    reverse_string += char.value

print(reverse_string)
print(stack.peek())

