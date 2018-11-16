# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:25:14 2018

@author: Abdullah Mobeen
"""

class Empty(Exception):
    """Error that will occur when attempting to access an element from an empty stack"""
    pass

class Stack:
    CAP =10
    """Implementation of Stack using an array"""

    def __init__(self):
        """creates an empty stack"""
        self._stackArray = []
        
    def __len__(self):
        """returns the length of the stack"""
        return len(self._stackArray)
    
    def top(self):
        """returns a reference to the top element without removing it.
        Throws an error if stack is empty"""
        if not self.is_empty():
            return self._stackArray[-1]
        else:
            raise Empty('Stack is empty')
    
    def is_empty(self):
        """checks if the stack is empty"""
        return self.__len__() == 0
    
    def pop(self):
        """removes the top element from the stack and returns it. 
        Throws an error if stack is empty"""
        if not self.is_empty():
            elem = self._stackArray.pop()
            return elem
        else:
            raise Empty('Stack is empty')
    
    def push(self, elem):
        """adds/pushes an element at the top of the stack"""
        self._stackArray.append(elem)
        
    def display(self):
        """displays the stack, which is otherwise a private attribute of Stack class"""
        print(self._stackArray)
        
        
if __name__ == "__main__":
    stack = Stack()
    for i in range(0,20,2): #push even numbers into the stack
        stack.push(i)
    stack.display()
    for i in range(7): #remove the top 7 elements
        stack.pop()
    stack.display()
    top = stack.top() #display the top element
    print(top)
    
    for i in range(7): #check if the code raises an error when you try to delete elements from an empty stack
        stack.pop()
