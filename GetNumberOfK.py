#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: GetNumberOfK
@time: 2021/2/18 10:06
@IDE: PyCharm
@desc: 统计一个数字在升序数组中出现的次数。
示例1
输入
[1,2,3,3,3,3,4,5],3
返回值
4
"""


# 方案一、直接使用 count 方法
class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)


# 方案二、便历并计数
class Solution1:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        con = 0
        for i in data:
            if i == k:
                con += 1
        return con


# 方案三、二分法
class Solution2:
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        l_count, r_count = self.GetLeftCount(data, k), self.GetRightCount(data, k)
        if l_count == -1 or r_count == -1:
            return 0
        return r_count - l_count + 1

    def GetLeftCount(self, data, k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            elif mid - 1 >= 0 and data[mid - 1] == k:
                end = mid - 1
            else:
                return mid
        return -1

    def GetRightCount(self, data, k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            elif mid + 1 < len(data) and data[mid + 1] == k:
                start = mid + 1
            else:
                return mid
        return -1




# s = Solution()
# s = Solution1()
s = Solution2()
data, k = [1, 2, 3, 3, 3, 3, 4, 5], 3
print(s.GetNumberOfK(data, k))
