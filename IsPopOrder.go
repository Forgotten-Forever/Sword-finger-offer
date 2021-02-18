//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: IsPopOrder
@time: 2020/12/30 10:46
@IDE: GoLand
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
*/

package main

import "fmt"

func Pop1(stack []int) []int {
	if len(stack) > 1 {
		return stack[:len(stack)-1]
	}else {
		return []int{}
	}

}

// 方法一
func IsPopOrder( pushV []int ,  popV []int ) bool {
	if pushV == nil || len(pushV) != len(popV){
		return false
	}
	var stack []int
	index := 0
	for _, num := range pushV {
		stack = append(stack, num)
		for {
			if n := len(stack)-1; stack[n] == popV[index] {
				index++
				stack = stack[0:n]
				if n == 0 {
					break
				}
			} else {
				break
			}
		}
	}
	return len(stack) == 0
}

func main() {
	arr1, arr2 := []int{1, 2, 3, 4, 5}, []int{4, 5, 3, 2, 1}
	fmt.Println(IsPopOrder(arr1, arr2))
}