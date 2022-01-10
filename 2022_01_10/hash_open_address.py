# 해쉬 구현 - sha256을 이용
import hashlib



class HashData:

    #해시 객체 생성 - 해시 테이블로 쓸 리스트 크기를 받아서 초기화
    def __init__(self,list_size = 16) -> None:
        self.list_size = int(list_size)
        #빈 버켓은 0으로 표기
        self.buckets = list([ 0 for _ in range(list_size)])

    #해시 함수 정의
    def hash_func(self,convert_key:int) -> int:
        return convert_key % self.list_size

    #받은 키값을 sha256을 적용
    def get_key(self,key:str) -> int:

        #sha256을 사용
        hash_object = hashlib.sha256()
        #해시 함수에 넣을 수 있게 바이트로 인코딩
        hash_object.update(key.encode())

        #int로 변환하기 위해 우선 16진수로 변환
        hex_data = hash_object.hexdigest()
        
        #int로 변환해서 반환
        return int(hex_data,16)

    #key,value추가 - 개방주소법
    def add_open_address(self,key:str,value) -> None:
        
        #입력받은 키값을 sha256을 통해서 int형의 숫자로 바꿔줌
        temp_key = self.get_key(key)

        #변환된 키를 해시함수에 넣어서 인덱스를 뽑아냄
        index_key = self.hash_func(temp_key)

        #충돌이 났다면, 값을 저장하려는데 이미 있음
        if self.buckets[index_key] != 0:
            for i in range(self.list_size):
                if self.buckets[i] == 0:
                    self.buckets[i] = [temp_key,value]
                
                #충돌이 났을때 sha256처리한 key 값이 같다면 같은값 이므로 value 수정
                elif self.buckets[i][0] == temp_key:
                    self.buckets[i][1] = value
        
        #충돌이 안났으면 그냥 저장
        else:
            self.buckets[index_key] = [temp_key,value]

    #key값으로 데이터 읽기- 개방주소법
    def read_open_address(self,key:str):
        temp_key = self.get_key(key)

        index_key = self.hash_func(temp_key)
        if self.buckets[index_key] != 0:
            for i in range(self.list_size):
                if self.buckets[i] != 0 and self.buckets[i][0] == temp_key:
                    return self.buckets[i][1]

            #끝까지 다 돌았는데 매칭되는 값이 없으면 None 반환
            else:
                return None
        
        else:
            return None

    #삭제- 개방주소법
    def del_open_address(self,key:str) -> None:

        temp_key = self.get_key(key)
        
        index_key = self.hash_func(temp_key)
        
        
        if self.buckets[index_key] != 0:
            for i in range(self.list_size):
                if self.buckets[i] != 0 and self.buckets[i][0] == temp_key:
                    self.buckets[i] = 0
                    return "Delete Success"
            
            else:
                return None
        
        else:
            return None


if __name__ == "__main__":
    #해시 테이블 생성
    hash_d = HashData(8)

    #데이터 추가
    hash_d.add_open_address("lee",1)
    hash_d.add_open_address("park",7)
    hash_d.add_open_address("kim",8)
    hash_d.add_open_address("lee2",5)
    hash_d.add_open_address("park2",4)
    # hash_d.add_open_address("kim2",3)
    
    #데이터 읽기
    assert hash_d.read_open_address("lee2") == 5
    # #데이터 삭제
    assert hash_d.del_open_address("park") == "Delete Success"

    #삭제 확인
    assert hash_d.read_open_address("park") == None

    

    


