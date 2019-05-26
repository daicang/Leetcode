package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// in order traversal example, not used here
func inOrderTraversal(curr *TreeNode, out chan int) {
	stack := []*TreeNode{}
	defer close(out)

	for {
		// Push all ->left->left to stack
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}

		for {
			if len(stack) == 0 {
				return
			}
			// Pop one
			curr = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			out <- curr.Val

			if curr.Right != nil {
				// fmt.Println("turn right at ", curr.Val)
				curr = curr.Right
				break
			}
		}
	}

}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil {
		return false
	}

	return isSameTree(p.Left, q.Left) && p.Val == q.Val && isSameTree(p.Right, q.Right)
}

func main() {
	t1 := &TreeNode{Val: 1}
	t2 := &TreeNode{Val: 1}

	t1.Left = &TreeNode{Val: 2}
	t2.Left = &TreeNode{Val: 2}

	t1.Right = &TreeNode{Val: 3}
	t2.Right = &TreeNode{Val: 3}

	fmt.Println(isSameTree(t1, t2))

	fmt.Println(isSameTree(nil, &TreeNode{Val: 0}))

	t1 = &TreeNode{Val: 10}
	t1.Left = &TreeNode{Val: 5}
	t1.Right = &TreeNode{Val: 15}

	t2 = &TreeNode{Val: 10}
	t2.Left = &TreeNode{Val: 5}
	t2.Left.Right = &TreeNode{Val: 15}

	fmt.Println(isSameTree(t1, t2))
}
