# 데모 실행용 코드     
 
N = 8
tree = {}

input = [["A", "B", "C"], ["B", "D", "."],["C", "E", "F"],
         ["C", "E", "F"], ["E", ".", "."], ["F", ".", "G"],
         ["D", ".", "."], ["G", ".", "."]]
 
for i in range(N):
    root, left, right = input[i][0], input[i][1], input[i][2]
    tree[root] = [left, right]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
print(tree)