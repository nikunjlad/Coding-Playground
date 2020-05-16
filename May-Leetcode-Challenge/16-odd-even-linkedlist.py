"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val)   # to print the Node values


class Solution:

    def __init__(self, head=None):
        self.head = head

    def print_list(self, head):
        """
        This will return entire linkedlist.
        """
        nodes = list()  # create empty list first
        curr = head  # current pointer is at the head of the list

        while curr:  # while current node has val and does not contains None, loop over
            nodes.append(repr(curr))  # append val of current node to the nodes list
            curr = curr.next  # now the current pointer shifts to the next node

        return '->'.join(nodes) + "->None"  # return list of all elements in the linkedlist

    def append(self, data):

        if not self.head:  # check if head is None
            self.head = ListNode(val=data)  # add first value to the head and return
            return

        curr = self.head  # if head is not None, head is the current node

        while curr.next:  # loop till the point we reach None
            curr = curr.next  # point next node to current pointer

        curr.next = ListNode(val=data)  # add new listnode at end of linkedlist having found None

    def oddEvenList(self, head: ListNode) -> ListNode:

        curr = head  # current node is the head of linkedlist
        values = list()  # initialize list to hold node values

        while curr:
            values.append(curr.val)  # append value of the current node
            curr = curr.next  # go to the next node

        i = 0  # start from index 0 for odd values
        curr = head  # point current node back to head again

        while i < len(values):
            curr.val = values[i]  # add odd values from the value list
            curr = curr.next  # move to next node
            i += 2  # increment counter by 2

        i = 1  # start from index 1 for even values
        while i < len(values):
            curr.val = values[i]  # add even values from the value list
            curr = curr.next  # next node
            i += 2  # increment counter by 2

        return head


s1 = Solution()
s1.append(1)
s1.append(2)
s1.append(3)
s1.append(4)
s1.append(5)
print("Original LinkedList: ", s1.print_list(s1.head))
oe = s1.oddEvenList(s1.head)
print("Odd-Even LinkedList: {}\n".format(s1.print_list(oe)))

s2 = Solution()
s2.append(2)
s2.append(1)
s2.append(3)
s2.append(5)
s2.append(6)
s2.append(4)
s2.append(7)
print("Original LinkedList: ", s2.print_list(s2.head))
oe = s2.oddEvenList(s2.head)
print("Odd-Even LinkedList: {}\n".format(s2.print_list(oe)))
