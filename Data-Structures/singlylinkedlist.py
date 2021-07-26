class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newnode

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None

            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def printlist(self):
        curnode = self.head
        while curnode != None:
            print(curnode.data, end=" ")
            curnode = curnode.next

    def len_iterative(self):
        len = 0
        curnode = self.head
        while (curnode is not None):
            len += 1
            curnode = curnode.next

        return (len)

    def count_occurrences_iterative(self, key):
        count = 0
        cur = self.head
        while cur:
            if cur.data == key:
                count += 1
            cur = cur.next

        print(count)

    def count_occurrences_recursive(self, node, key):
        if not node:
            return 0

        if node.data == key:
            return 1 + self.count_occurences_recursive(node.next, key)
        else:
            return self.count_occurences_recursive(node.next, key)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1

        p = prev
        while q:
            prev = q
            q = q.next

        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    def print_nth_from_last(self, n):
        tot_len = self.len_iterative()
        cur = self.head
        while cur:
            if tot_len == n:
                return (cur.data)

            tot_len -= 1
            cur = cur.next


llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(3)
llist.append(4)
llist.append(0)
llist.append(2)
llist.append(8)

llist.rotate(4)
llist.printlist()
