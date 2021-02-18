//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: FindNumsAppearOnce
@time: 2021/2/18 11:57
@IDE: GoLand
@desc: 数组中只出现一次的数字 [位运算/哈希]
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
*/

package main

import "fmt"

func FindNumsAppearOnce(nums []int) []int {
	//返回[a,b] 其中ab是出现一次的两个数字
	// 异或: 任何一个数字异或它自己都等于0
	mp := map[int]int{}
	res := []int{}
	for _, v := range nums {
		mp[v]++
	}
	fmt.Println(mp)
	for k, v := range mp {
		if v == 1 {
			res = append(res, k)
		}
	}
	if res[1] < res[0] {
		res[0], res[1] = res[1], res[0]
	}
	return res
}

func main() {
	arr := []int{22, 1, 3, 5, 3, 22, 1, 8}
	fd := FindNumsAppearOnce(arr)
	fmt.Println(fd)
}