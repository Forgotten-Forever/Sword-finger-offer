#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Merge_LinkedList
@time: 2020/12/30 9:03
@IDE: PyCharm
@desc: 合并两个排序的链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
示例1
输入
{1,3,5},{2,4,6}
返回值
{1,2,3,4,5,6}
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        arr = ListNode(0)
        self.Step(pHead1, pHead2, arr)
        return arr.next

    def Step(self, pHead1, pHead2, arr):
        if not pHead1:
            arr.next = pHead2
            return None
        if not pHead2:
            arr.next = pHead1
            return None
        if pHead1.val > pHead2.val:
            arr.next = pHead2
            self.Step(pHead1, pHead2.next, arr.next)
        else:
            arr.next = pHead1
            self.Step(pHead1.next, pHead2, arr.next)
        # print(arr.val)


# 方法二
class Solution1:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        arr = ListNode(0)
        if pHead1.val > pHead2.val:
            arr = pHead2
            arr.next = self.Merge(pHead1, pHead2.next)
        else:
            arr = pHead1
            arr.next = self.Merge(pHead1.next, pHead2)
        return arr



arr1 = ListNode(1)
arr1.next = ListNode(3)
arr1.next.next = ListNode(5)
arr2 = ListNode(2)
arr2.next = ListNode(4)
arr2.next.next = ListNode(6)

s = Solution()
# s = Solution1()
c = s.Merge(arr1, arr2)
while c:
    print(c.val)
    c = c.next
