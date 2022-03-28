# Tree

import sys
input = sys.stdin.readline

def to_post_order(preorder, inorder):
    if len(preorder) == 0:
        return
    # 재귀를 종료하기 위한 조건들. 
    elif len(preorder) == 1:
        print(preorder[0], end= ' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end = ' ')
        return 
    # index 함수로 전위순회의 첫번째 즉 루트에 해당하는 값을 
    # 중위 순회의 리스트에서 찾아내어 이를 인덱스로 지정한다. 
    root_idx = inorder.index(preorder[0])
    left_in = inorder[0:root_idx]
    left_pre = preorder[1:1 + len(left_in)]
    to_post_order(left_pre, left_in)

    right_in = inorder[root_idx+1:]
    right_pre = preorder[len(left_pre) + 1:]
    to_post_order(right_pre, right_in)

    print(preorder[0], end= ' ')

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        preorder = list(map(int, input().split()))
        inorder = list(map(int, input().split()))

        to_post_order(preorder, inorder)
        print()