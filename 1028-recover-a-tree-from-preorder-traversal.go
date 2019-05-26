package main

import (
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverFromPreorder(S string) *TreeNode {
	type Pair struct {
		node  *TreeNode
		depth int
	}

	var stack []Pair
	var num string
	var depth int

	S += "-"
	for _, ch := range S {
		if string(ch) == "-" {
			if len(num) != 0 {
				val, _ := strconv.Atoi(num)
				num = ""
				curr := TreeNode{Val: val}
				pair := Pair{node: &curr, depth: depth}

				if len(stack) != 0 {
					top := stack[len(stack)-1]
					if top.depth == depth-1 {
						top.node.Left = &curr
					} else {
						for top.depth >= depth {
							stack = stack[:len(stack)-1]
							top = stack[len(stack)-1]
						}
						top.node.Right = &curr
					}
				}
				stack = append(stack, pair)
				depth = 0
				num = ""
			}
			depth++
		} else {
			num += string(ch)
		}
	}
	return stack[0].node
}

func main() {
	recoverFromPreorder("1-2--3--4-5--6--7")
}
