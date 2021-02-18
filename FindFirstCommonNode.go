//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: FindFirstCommonNode
@time: 2021/1/26 19:05
@IDE: GoLand
@desc: 输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
*/

package main

import "fmt"

type ListNode struct{
	Val int
	Next *ListNode
}

/**
 *
 * @param pHead1 ListNode类
 * @param pHead2 ListNode类
 * @return ListNode类
 */

// 方法一、存入列表依次 弹出对比
func FindFirstCommonNode( pHead1 *ListNode ,  pHead2 *ListNode ) *ListNode {
	if pHead1 == nil && pHead2 == nil{
		return nil
	}
	var pList2 []ListNode
	var pList1 []ListNode
	for pHead1 != nil{
		pList1 = append(pList1, *pHead1)
		pHead1 = pHead1.Next
	}
	for pHead2 != nil{
		pList2 = append(pList2, *pHead2)
		pHead2 = pHead2.Next
	}
	//for i := 0; i < len(pList1); i ++{
	//	fmt.Println(pList1[i].Val)
	//}
	//for i := 0; i < len(pList2); i ++{
	//	fmt.Println(pList2[i].Val)
	//}
	var tmp *ListNode
	length1, length2 := len(pList1)-1, len(pList2)-1
	for length1 >= 0 && length2 >= 0{
		pNode1, pNode2 := pList1[length1], pList2[length2]
		//fmt.Println(pNode1, pNode2)
		if pNode1.Val == pNode2.Val{
			tmp = &pNode1
		}else{
			break
		}
		length1 -= 1
		length2 -= 1
	}
	return tmp
}

// 方法二、通过 链表 pHead1 与 pHead2 之间互相拼接，使 p1、p2一直循环直到公共节点 停止循环
func FindFirstCommonNode1( pHead1 *ListNode ,  pHead2 *ListNode ) *ListNode {
	if pHead1 == nil || pHead2 == nil{
		return nil
	}
	arr1, arr2 := pHead1, pHead2
	for arr1 != arr2 {
		if arr1 == nil {
			arr1 = pHead2
		}else{
			arr1 = arr1.Next
		}
		if arr2 == nil {
			arr2 = pHead1
		}else {
			arr2 = arr2.Next
		}
	}
	return arr1
}

func main() {
	// pHead1 [1, 3, 5, 6, 7, 8, 9]
	// pHead2 [2, 4, 6, 7, 8, 9]
	pHead1 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 3,
			Next: &ListNode{
				Val: 5,
				Next: &ListNode{
					Val: 6,
					Next: &ListNode{
						Val: 7,
						Next: &ListNode{
							Val: 8,
							Next: &ListNode{
								Val: 9,
								Next: nil,
							},
						},
					},
				},
			},
		},
	}

	pHead2 := &ListNode{
		Val: 2,
		Next: &ListNode{
			Val: 4,
			Next: &ListNode{
				Val: 6,
				Next: &ListNode{
					Val: 7,
					Next: &ListNode{
						Val: 8,
						Next: &ListNode{
							Val: 9,
							Next: nil,
						},
					},
				},
			},
		},
	}
	pHead3 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 3,
				Next: &ListNode{
					Val: 4,
					Next: nil,
				},
			},
		},
	}
	pHead4 := &ListNode{
		Val: 5,
		Next: &ListNode{
			Val: 6,
			Next: &ListNode{
				Val: 7,
				Next: nil,
			},
		},
	}

	arr := FindFirstCommonNode(pHead1, pHead2)
	arr1 := FindFirstCommonNode(pHead3, pHead4)
	fmt.Println(arr, arr1)
	arr2 := FindFirstCommonNode1(pHead1, pHead2)
	arr3 := FindFirstCommonNode1(pHead3, pHead4)
	fmt.Println(arr2, arr3)
}