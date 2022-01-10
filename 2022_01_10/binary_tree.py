#이진 트리 


#노드 정의
class Node:

    def __init__(self,data:int):
        self.data = data
        self.left = None
        self.right = None

#이진 트리 

class BinaryTree:

    def __init__(self):
        self.root = None

    #노드 전위순회 : 루트-> 왼쪽 -> 오른쪽
    def pre_order(self,node):
        if node != None:
            #루트 방문
            print(node.data,end=" ")
            if node.left != None:
                self.pre_order(node.left)

            if node.right != None:
                self.pre_order(node.right)

        else:
            return 

    #후위 순회 : 왼쪽 -> 오른쪽 -> 루트
    def post_order(self,node):
        if node != None:

            if node.left != None:
                self.post_order(node.left)
        
            if node.right != None:
                self.post_order(node.right)
            print(node.data,end=" ")
        else:
            return 

    
    def in_order(self,node):
        if node != None:

            if node.left != None:
                self.in_order(node.left)

            print(node.data,end=" ")

            if node.right != None:
                self.in_order(node.right)
            
        else:
            return 

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8

    binary_tree = BinaryTree()
    
    #전위 순회
    binary_tree.pre_order(node1)
    print("\n1 2 4 8 5 3 6 7")

    #후위 순회
    binary_tree.post_order(node1)
    print("\n8 4 5 2 6 7 3 1")
    
    #중위 순회
    binary_tree.in_order(node1)
    print("\n8 4 2 5 1 6 3 7")

