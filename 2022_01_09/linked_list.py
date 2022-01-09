#Single LinkedList 구현

#노드
class Node:

    def __init__(self,data, next = None):
        self.data = data
        self.next = None

#노드관리 (추가, 삭제, 모든값 출력,탐색)
class NodeManage:

    #첫 생성
    def __init__(self, data):
        self.head = Node(data)

    #노드 추가
    def add(self,data):
        #head에 없다면
        if self.head == '':
            self.head = Node(data)
        #head가 있다면(초기생성 이미 함)
        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(data)
    
    def delete(self,data):

        if self.head == None:
            print("not found node")
            return
        
        elif self.head.data == data:
            temp = self.head
            self.head = self.head.next

            del temp

        #head가 아닌 노드 삭제할떄   
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

    #노드 순회하면서 값 출력
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    #노드에서 원하는 노드찾기
    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        
if __name__ == "__main__":

    #링크드 리스트에 추가
    print("생성")
    linked_list = NodeManage(1)
    linked_list.desc()

    print("추가")
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.desc()

    print("삭제")
    linked_list.delete(3)
    linked_list.desc()

    print("탐색")
    node = linked_list.search(4)
    print(node.data)


