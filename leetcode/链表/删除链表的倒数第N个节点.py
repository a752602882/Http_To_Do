
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        length = 0
        p = head

        while p:  #遍历操作
            length += 1
            p = p.next

        idx = length - n #要删除的位置
        #pre.next = pre.next.next 可以删除指定位置

        p = head #重新赋值

        if idx == 0:
            return p.next

        for i in range(length):
            if i == idx - 1: #删除位置的前一个位置，
                p.next = p.next.next #删除指定位置
                return head
            else:
                p = p.next #继续遍历


if __name__ =='__main__':
    head = [1,2,3,4,5]
    Solution().removeNthFromEnd(head,3)
    print(head)