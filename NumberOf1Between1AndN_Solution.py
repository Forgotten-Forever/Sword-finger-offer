#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: NumberOf1Between1AndN_Solution
@time: 2021/1/5 9:35
@IDE: PyCharm
@desc: 整数中 1 出现的次数
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
输入
13
返回值
6
"""


# 方法一、将 数 转化为 字符串再转化为 列表，求列表内 1 的数量
# 浪费时间与空间
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(1, n+1):
            i = list(str(i))
            count += i.count('1')
        return count


# 方法二、
class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):
        i = 1
        count = 0
        while i <= n:
            # x 为 取整后的值
            x = n // (i * 10) * i
            # 余数
            condition = n % (i * 10)
            if condition >= 2 * i - 1:
                count += x + i
            elif condition < i:
                count += x
            else:
                count += x + condition - i + 1
            i = i * 10
        return count


# s = Solution()
s = Solution1()
print(s.NumberOf1Between1AndN_Solution(13))