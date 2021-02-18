#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Binary_tree_to_bidirectional_list
@time: 2021/1/5 9:00
@IDE: PyCharm
@desc: 二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法一、中序遍历得到排序好的列表，在列表中创建双向关系
class Solution:
    # stack = []

    def __init__(self):
        self.stack = []

    def Convert(self, pRootOfTree):
        # 先进性中序遍历, 中序遍历是有序的
        if not pRootOfTree:
            return None
        self.dfs(pRootOfTree)
        # 得到中序遍历 stack, 建立双向链表之间的双线联系
        for i in range(1, len(self.stack)):
            self.stack[i - 1].right = self.stack[i]
            self.stack[i].left = self.stack[i - 1]
        return self.stack[0]

    def dfs(self, node):
        if not node:
            return None
        if node.left:
            self.dfs(node.left)
        self.stack.append(node)
        if node.right:
            self.dfs(node.right)


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(7)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(8)
s = Solution()
print(s.Convert(tree))