//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: GetNumberOfK
@time: 2021/2/18 10:14
@IDE: GoLand
@desc: 统计一个数字在升序数组中出现的次数。
示例1
输入
[1,2,3,3,3,3,4,5],3
返回值
4
*/

package main

import (
	"fmt"
)

// 计数法统计
func GetNumberOfK( data []int ,  k int ) int {
	if data == nil{
		return 0
	}
	con := 0
	for i := 0; i< len(data); i ++ {
		if data[i] == k {
			con += 1
		}
	}
	return con
}

// 二分法统计
func GetNumberOfK1( data []int ,  k int ) int {
	if len(data) == 0{
		return 0
	}
	l_count, r_count := GetLeftCount(data, k), GetRightCount(data, k)
	if l_count == -1 || r_count == -1 {
		return 0
	}
	return r_count - l_count + 1
}

func GetLeftCount(data []int, k int) int {
	start, end := 0, len(data) - 1
	for start <= end {
		mid := (start + end) / 2
		// 升序数组
		if data[mid] > k{
			end = mid - 1
		}else if data[mid] < k {
			start = mid + 1
		}else if mid - 1 >= 0 && data[mid - 1] == k {
			end = mid - 1
		}else{
			return mid
		}
	}
	return -1
}

func GetRightCount(data []int, k int) int {
	start, end := 0, len(data) - 1
	for start <= end {
		mid := (start + end) / 2
		// 升序数组
		if data[mid] > k{
			end = mid - 1
		}else if data[mid] < k {
			start = mid + 1
		}else if mid + 1 < len(data) && data[mid + 1] == k {
			start = mid + 1
		}else{
			return mid
		}
	}
	return -1
}

func main() {
	data, k := []int{3,3,3,3}, 3
	gt := GetNumberOfK(data, k)
	gt1 := GetNumberOfK1(data, k)
	fmt.Println(gt)
	fmt.Println(gt1)
}
