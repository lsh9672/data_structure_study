#이진 탐색 트리

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self,data):
        self.head = Node(data)

    #데이터 추가
    def add(self,data:int) -> None:
        self.current_node = self.head
        while True:
            #현재 노드와 비교해서 값이 작으면 왼쪽
            if data < self.current_node.data:
                #왼쪽 노드가 있으면 해당 노드를 현재노드에 넣고 비교 반복
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                    continue
                #왼쪽에 노드가 없으면 그대로 추가
                else:
                    self.current_node.left = Node(data)
                    break

            #크면 오른쪽
            elif data > self.current_node.data:
                
                #오른쪽 노드가 존재하면 해당노드를 현재노드에 넣고 비교 반복
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                    continue
                #없으면 그냥 추가
                else:
                    self.current_node.right = Node(data)
                    break 
            #값이 같으면 - bst는 중복을 허용안함(노드수가 늘어나면 탐색시간이 증가하기 때문에)
            else:
                pass

    #트리에서 노드 검색
    def search(self,data:int) -> bool:
        self.current_node = self.head

        while self.current_node != None:
            #작으면 왼쪽으로 탐색
            if data < self.current_node.data:
                self.current_node = self.current_node.left
                continue
            #크면 오른쪽으로 탐색
            elif data > self.current_node.data:
                self.current_node = self.current_node.right

            #같으면 리턴
            else:
                return True

        #끝까지 돌았는데 없으면 False        
        else:
            return False

    def delete(self,data:int) -> bool:
        #현재 노드와 부모노드를 저장하고 있어야 현재노드가 삭제 되었을때 부모노드에 자식노드 연결가능
        self.current_node = self.head
        self.parent_node = self.head

        #주어진 값이 삭제해야될 값인지 
        search_check = False

        #탐색
        while self.current_node != None:

            if data < self.current_node.data:
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
                continue
            elif data > self.current_node.data:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right
            #같으면 체크값 true
            else:
                search_check = True
                break
        
        #매칭되는 값이 없으면 종료
        if search_check == False:
            return False

        #자식 노드가 없는 경우
        if self.current_node.left == None and self.current_node.right == None:
            if data < self.parent_node.data:
                self.parent_node.left = None
            else:
                self.parent_node.right = None

        #자식노드가 한개인 경우 - 왼쪽에만 있을때
        elif self.current_node.left != None and self.current_node.right == None:
            #삭제하려고 하는 노드가 부모의 왼쪽
            if data < self.parent_node.data:
                self.parent_node.left = self.current_node.left
            #삭제하려고 하는 노드가 부모의 오른쪽
            else:
                self.parent_node.right = self.current_node.left
        #자식노드가 한개인 경우 - 오른쪽에만 있을때
        elif self.current_node.left == None and self.current_node.right != None:
            #삭제하려고 하는 노드가 부모의 왼쪽
            if data < self.parent_node.data:
                self.parent_node.left = self.current_node.right
            #삭제하려고 하는 노드가 부모의 오른쪽
            else:
                self.parent_node.right = self.current_node.right
        
        #삭제하려고 하는 노드에 자식노드가 두개일때
        elif self.current_node.left != None and self.current_node.right != None:
            #바꿀 노드 탐색
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right

            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left

            #바꿀노드를 탐색하다 바꿀노드의 왼쪽이 없을떄 까지 왔는데 오른쪽이 있으면 바꿀노드가 가장 작은 노드
            if self.change_node.right != None:
                self.change_node_parent = self.change_node.right
            #바꿀노드에 오른쪽이 없다면, 즉 자식이 없으면 그냥 자기 자신
            else:
                self.change_node_parent.left = None
            
            #삭제할 값이 부모의 왼쪽에 있을때
            if data < self.parent_node.data:
                self.parent_node.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

            #삭제할 값이 부모의 오른쪽일때
            else:
                self.parent_node.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        return True    

if __name__ == "__main__":

    #bst생성
    bst = BST(10)
    
    #노드 추가
    bst.add(5)
    bst.add(6)
    bst.add(11)
    bst.add(8)  
    bst.add(15)

    #원하는 노드 탐색
    assert bst.search(11) == True

    assert bst.delete(11) == True

    assert bst.search(11) == False

    

    
    

            