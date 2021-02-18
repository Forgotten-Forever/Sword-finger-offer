#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: FindFirstCommonNode
@time: 2021/1/26 17:49
@IDE: PyCharm
@desc: 输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类


# 方法一、分别遍历两个链表，将每个链表存储至对应的列表内，对列表进行 pop 操作，第一对不相同节点的 next 即是公共节点
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return None
        pList1, pList2 = [], []
        tmp = ListNode(None)
        while pHead1:
            pList1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            pList2.append(pHead2)
            pHead2 = pHead2.next
        # 输出 两个列表内数值
        # print([x.val for x in pList1], [x.val for x in pList2])
        for node in range(min(len(pList1), len(pList2))):
            pNode1 = pList1.pop()
            pNode2 = pList2.pop()
            # 输出 弹出值
            # print(pNode1.val, pNode2.val)
            if pNode2.val == pNode1.val:
                tmp = pNode1
            else:
                break
        return tmp


# 方法二、通过 链表 pHead1 与 pHead2 之间互相拼接，使 p1、p2一直循环直到公共节点 停止循环
class Solution1:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            """
            第一轮循环:
                1, 2, 3, 4, 5, 6, 结束第一轮 p2 = Phead1, p1 = p1.next = 9
            p1: 1, 3, 5, 6, 7, 8   
            p2: 2, 4, 6, 7, 8, 9   
            第二轮循环 p2 = Phead1, p1 = p1.next = 9 对比一次后 p1 = pHead2:
                1, 2(p1=Phead2),   3,  4(p1 = p2 对比结束)
            p1: 9,      2,         4,  6
            p2: 1,      3,         5,  6
            返回 p1 此时 p1 = [6, 7, 8, 9]
            """
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        print(type(p1))
        return p1


# pHead1 [1, 3, 5, 6, 7, 8, 9]
# pHead2 [2, 4, 6, 7, 8, 9]
pHead1 = ListNode(x=1)
pHead1.next = ListNode(3)
pHead1.next.next = ListNode(5)
pHead1.next.next.next = ListNode(6)
pHead1.next.next.next.next = ListNode(7)
pHead1.next.next.next.next.next = ListNode(8)
pHead1.next.next.next.next.next.next = ListNode(9)

pHead2 = ListNode(2)
pHead2.next = ListNode(4)
pHead2.next.next = ListNode(6)
pHead2.next.next.next = ListNode(7)
pHead2.next.next.next.next = ListNode(8)
pHead2.next.next.next.next.next = ListNode(9)

# s = Solution()
# print(s.FindFirstCommonNode(pHead1, pHead2).val)
s1 = Solution1()
print(s1.FindFirstCommonNode(pHead1, pHead2))
