#큐의 enqueue, dequeue 함수 구현하기

class Queue:
    queue = None
    #큐 생성
    def __init__(self,queue = list()):
        self.queue = queue

    #큐 현재 상태 보기
    def status(self) -> list:
        return self.queue

    #큐 현재 길이
    def length(self) -> int:
        return len(self.queue)

    #enqueue
    def enqueue(self,data:int):
        self.queue.append(data)

    #dequeue
    def dequeue(self):
        #값이 있을때만 queue
        if len(self.queue) > 0:
            del self.queue[0]


if __name__ == "__main__":

    #큐 생성
    queue = Queue()
    print(f"queue status : {queue.status()}, queue length : {queue.length()}")

    #enqueue
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"queue status : {queue.status()}, queue length : {queue.length()}")

    #dequeue
    queue.dequeue()
    print(f"queue status : {queue.status()}, queue length : {queue.length()}")




