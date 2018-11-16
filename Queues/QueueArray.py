# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 20:50:40 2018

@author: Abdullah Mobeen
"""

class Error(Exception):
    """Error that will occur when attempting to access an element from an empty queue"""
    pass

class Queue:
    """Implementation of Queue using an Array. Using just an ordinary array would be
    troublesome as the dequeue option - removing the first element - would require shifting
    all the other elements one index back, prompting a O(n) dequeue. Instead we use
    a circular array where we don't move elements but just the markers"""
    
    CAPACITY = 10     
    
    def __init__(self):
        """creates a list of size CAPACITY with Nones'
        sets two markers:
            self._size indicates how many non-None elements are in the Queue
            self._first is the index of the first element in the queue"""
            
        self._data = [None] * Queue.CAPACITY
        self._size = 0 
        self._first = 0 
        
    def __len__(self):
        """returs the number of elements in the queue"""
        return self._size
        
    def first(self):
        """returns the first element of the queue"""
        if not self.is_empty():
            return self._data[self._first]
        else:
            raise Error("Queue is empty")
    
    def is_empty(self):
        """returns True if the queue is empty, False otherwise"""
        return self._size == 0
        
    def dequeue(self):
        """removes the first element from the queue if the queue is not empty and returns it.
        if the number of elements becomes less than half of the size of the queue 
        i.e. more than half the list is just None elements, then downsize the list"""
        if self.is_empty():
            raise Error("Queue is empty")
        elem = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % len(self._data)
        self._size -= 1
        if self._size <= int((1/2)*len(self._data)):
            self.resize(int((1/2)*len(self._data)))
        
        return elem
    
    def enqueue(self, elem):
        """adds elem at the back of the queue. 
        If the number of elements in the queue becomes equal to the length of the array,
        then we resize the array (increase capacity)"""
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        new_ind = (self._first + self._size) % len(self._data)
        self._data[new_ind] = elem
        self._size += 1
        
    def resize(self, new_size):
        """resizes the array to new_size and copies the elements here"""
        old = self._data 
        self._data = [None] * new_size 
        marker = self._first
        for k in range(self._size): 
            self._data[k] = old[marker] 
            marker = (1 + marker) % len(old)
        self._first = 0
        
    def display(self):
        """displays the queue, which is otherwise a private attribute of Queue class"""
        print(self._data)
        
        
if __name__ == "__main__":
    q = Queue()
    
    for i in range(0,20,2):
        q.enqueue(i)
    q.display()
    
    for i in range(3):
        q.enqueue(i)
    q.display()
    
    for i in range(5):
        q.dequeue()
    q.display()
    print(q.first())
    for i in range(7):
        q.dequeue()
    q.display()

    