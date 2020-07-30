class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)  # 头结点，无存储，指向链表第一个结点,用于返回
    node = head  # 初始化链表结点
    carry = 0  # 初始化 进一 的数
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = x + y + carry  # 对每一位求和
        carry = sum // 10  # 地板除，求进一（其为0或1）
        node.next = ListNode(sum % 10)  # 取余数，求本位结点
        if l1:  # 求空否，防止出现无后继结点
            l1 = l1.next
        if l2:  # 同上
            l2 = l2.next
        node = node.next  # 更新指针
    if carry != 0:  # 验证最后一位相加是否需 进一
        node.next = ListNode(1)
    return head.next  # 返回头结点的下一个结点，即链表的第一个结点


if __name__ == "__main__":
    l1 = ListNode(2)
    # l1.next = ListNode(4)
    node = l1
    node.next = ListNode(4)
    node = node.next
    node.next = ListNode(3)
    # l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    a = addTwoNumbers(l1, l2)
    while a:
        print("%d" % a.val)
        a = a.next
