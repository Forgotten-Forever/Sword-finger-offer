//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: Binary_tree_to_bidirectional_list
@time: 2021/1/5 9:16
@IDE: GoLand
@desc: 二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
*/

package main

import "fmt"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

// 先进行中序遍历，在进行双线链表关系的建立
func Convert( pRootOfTree *TreeNode ) *TreeNode {
	if pRootOfTree == nil {
		return nil
	}
	stack := dfs(pRootOfTree)
	for i := 1; i < len(stack); i ++ {
		stack[i-1].Right = stack[i]
		stack[i].Left = stack[i-1]
	}
	return stack[0]
}

// 中序遍历
func dfs(node *TreeNode) (stack []*TreeNode) {
	if node == nil {
		return nil
	}
	stack = append(dfs(node.Left), node)
	stack = append(stack, dfs(node.Right)...)
	return stack
}

func main() {
	leftLeft := TreeNode{
		Val: 2,
	}
	leftRight := TreeNode{
		Val: 4,
	}
	left := TreeNode{
		Val:   3,
		Left:  &leftLeft,
		Right: &leftRight,
	}
	rightLeft := TreeNode{
		Val: 6,
	}
	rightRight := TreeNode{
		Val: 8,
	}
	right := TreeNode{
		Val: 7,
		Left: &rightLeft,
		Right: &rightRight,
	}
	tree := TreeNode{
		Val: 5,
		Left: &left,
		Right: &right,
	}
	fmt.Println(Convert(&tree))
}