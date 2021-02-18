//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: NumberOf1Between1AndN_Solution
@time: 2021/1/5 11:05
@IDE: GoLand
@desc: 整数中 1 出现的次数
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
输入
13
返回值
6
*/

package main

import "fmt"

func NumberOf1Between1AndN_Solution( n int ) int {
	i, count := 1, 0
	for i <= n{
		// 取整
		x := n / (i * 10) * i
		// 余数
		con := n % (i * 10)
		if con < i{
			count += x
		}else if con >= 2 * i - 1 {
			count += x + i
		}else {
			count += x + con + 1 - i
		}
		i = i * 10
	}
	return count
}

func main() {
	fmt.Println(NumberOf1Between1AndN_Solution(10000))
}