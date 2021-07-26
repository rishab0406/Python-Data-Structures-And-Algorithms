from collections import deque

class Stack:
    def __init__(self):
        self.items=deque()
        
    def push(self,val):
        self.items.append(val)

    def is_empty(self):
        return len(self.items)==0
        
    def pop(self):
        if self.is_empty():
          return "Stack is empty"
        return self.items.pop() 
    
    def peek(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)

def is_balanced(string):
    s=Stack()
    a="({["
    check=True
    for ch in string:
        if ch in a:
            s.push(ch)
        
        if ch==")":
            if s.pop()=="(":
                check=True
            else:
                check=False
        
        if ch=="}":
            if s.pop()=="{":
                check=True
            else:
                check=False

        if ch=="]":
            if s.pop()=="[":
                check=True
            else:
                check=False


    print(check)

if __name__ == '__main__':
    is_balanced("({a+b})") 
    is_balanced("))((a+b}{") 
    is_balanced("[a+b]*(x+2y)*{gg+kk}")
    