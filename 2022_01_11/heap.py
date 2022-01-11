#힙 구현

#힙은 구조상 트리처럼 노트가 이어진형태지만, 실제로 구현할때는 배열로 구현한다.
class Heap:

    #힙은 편의상 인덱스1번부터 사용하기 때문에 첫번째에 None을 넣어준다.
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    #부모랑 우선순위 비교해서 올릴지 말지 결정 - True면 부모보다 자식이 우선순위가 높기때문에 바꿈
    def move_check(self,index):
        #루트이므로 False
        if index <=1:
            return False

        #부모의 인덱스는 자식 인덱스의 절반
        parent_index = index // 2

        #자식이 우선순위가 크면(max heap을 기준으로 함.)
        if self.heap_array[index] > self.heap_array[parent_index]:
            return True

        else:
            return False

    #데이터를 뺐으면 다시 우선순위에 맞게 정렬해둬야됨.
    def pop_check(self,index):
        left_child_index = index * 2
        right_child_index = (index*2)+1

        #왼쪽 노드가 있는지 확인 - 완전이진탐색이라 왼쪽이 없으면 오른쪽도 없음
        if left_child_index >= len(self.heap_array):
            return False
        
        #오른쪽 노드가 있는지 확인 - 오른쪽이 있으면 왼쪽도 있으니까 확인해야됨.
        elif right_child_index >= len(self.heap_array):
            #왼쪽값 확인
            if self.heap_array[index] < self.heap_array[left_child_index]:
                return True
            
            else:
                return False
        
        #양쪽에 다 있다면
        else:
            #왼쪽이 오른쪽 보다 크다면
            if self.heap_array[left_child_index] < self.heap_array[right_child_index]:
                #팝되어서 맨위로 올라온 값과 비교
                if self.heap_array[index] < self.heap_array[left_child_index]:
                    return True
                else:
                    return False
            #오른쪽이 왼쪽보다 크다면
            else:
                if self.heap_array[index] < self.heap_array[right_child_index]:
                    return True
                else:
                    return False  
    #데이터 삽입
    def add(self,data):
        #힙에 값이 하나만 들어있으면 아무것도 없다는 뜻(첫번째값이 None)
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        
        self.heap_array.append(data)

        #마지막 값의 인덱스 확인
        inserted_index = len(self.heap_array) - 1

        #우선순위가 정렬될떄까지 반복
        while self.move_check(inserted_index):
            #반복문이 실행되면 넣으려고 하는 자식이 부모보다 우선순위가 높다는 뜻
            parent_index = inserted_index // 2
            self.heap_array[parent_index], self.heap_array[inserted_index] = self.heap_array[inserted_index], self.heap_array[parent_index]
            inserted_index = parent_index

        return True

    def pop(self):

        #힙이 비어있다면 pop할 것이 없음
        if len(self.heap_array) <=1:
            return None
        
        return_data = self.heap_array[1]

        #뻈으면 일단 가장 마지막 값을 맨위로 올림
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        pop_index = 1

        while self.pop_check(pop_index):
            left_child_index = pop_index * 2
            right_child_index = (pop_index * 2) + 1
            #오른쪽이 없으면 왼쪽은 있음(pop_check함수로 검증)
            if right_child_index >= len(self.heap_array):
                self.heap_array[pop_index],self.heap_array[left_child_index] = self.heap_array[left_child_index],self.heap_array[pop_index]
                pop_index = left_child_index
            #있으면 두개 비교
            else:
                #왼쪽이 크다면 왼쪽하고 자리바꾸기
                if self.heap_array[left_child_index] > self.heap_array[right_child_index]:
                    self.heap_array[pop_index],self.heap_array[left_child_index] = self.heap_array[left_child_index],self.heap_array[pop_index]
                    pop_index = left_child_index

                else:
                    self.heap_array[pop_index],self.heap_array[right_child_index] = self.heap_array[right_child_index],self.heap_array[pop_index]
                    pop_index = right_child_index

        return return_data

if __name__ == "__main__":
    heap = Heap(15)
    heap.add(10)
    heap.add(8)
    heap.add(5)
    heap.add(4)
    heap.add(20)
    assert heap.heap_array == [None, 20, 10, 15, 5, 4, 8]

    assert heap.pop() == 20

    assert heap.heap_array == [None, 15, 10, 8, 5, 4]