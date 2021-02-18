#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: IsPopOrder
@time: 2020/12/30 10:32
@IDE: PyCharm
@desc: 栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
输入
[1,2,3,4,5],[4,3,5,1,2]
返回值
false
"""


# 方法一、通过 空列表 实现压入的过程，当压入过程中 最后一个值 与 POP 列表内第一个值相等 说明此时弹出 POP ，
# 栈内 弹出 此值， POP 列表内 索引 +1 或者 弹出第一个值，如果满足栈的条件 最终 弹出结束后 栈为空
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or len(pushV) != len(popV):
            return None
        stack = []
        index = 0
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[index]:
                stack.pop()
                index += 1
        if stack:
            return False
        else:
            return True


s = Solution()
arr1, arr2 = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
print(s.IsPopOrder(arr1, arr2))
