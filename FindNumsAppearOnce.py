#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: FindNumsAppearOnce
@time: 2021/2/18 10:52
@IDE: PyCharm
@desc: 数组中只出现一次的数字 [位运算/哈希]
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


# 方案一、数组操作
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        pt = []
        for num in array:
            if array.count(num) == 1:
                pt.append(num)
        return pt


class Solution1:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        arr = set(array)
        pt = []
        for i in arr:
            con = 0
            for num in array:
                if i == num :
                    con += 1
            if con == 1:
                pt.append(i)
        return pt


# 异或: 任何一个数字异或它自己都等于0
class Solution2:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        arr = set(array)
        pt = []
        for n in arr:
            con = 0
            for num in array:
                if n ^ num == 0:
                    con += 1
            print(con)
            if con == 1:
                pt.append(n)
        return pt


# s = Solution()
# s = Solution1()
s = Solution2()
arr = [22, 1, 3, 5, 3, 22, 1, 8]
print(s.FindNumsAppearOnce(arr))