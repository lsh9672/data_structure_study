#스택의 pop, push 구현

class Stack:
    stack = None
    #스택 생성
    def __init__(self,stack=list()):
        self.stack = stack
    
    #스택 상태보기
    def status(self) -> list:
        return self.stack

    #스택 길이
    def length(self) -> int:
        return len(self.stack)

    #push 구현
    def push(self,data:int):
        self.stack.append(data)

    #pop구현
    def pop(self):
        #값이 있을떄만 pop
        if len(self.stack) > 0:
            del self.stack[-1]



if __name__ == "__main__":
    #스택생성
    stack = Stack()
    print(f"stack status : {stack.status()}, stack length : {stack.length()}")

    #값넣기
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"stack status : {stack.status()}, stack length : {stack.length()}")

    stack.pop()
    print(f"stack status : {stack.status()}, stack length : {stack.length()}")


