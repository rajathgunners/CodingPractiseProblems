from stack import Stack

class Queue(Stack):
    def __init__(self):
        super().__init__()
    
    
    def insertion(self, val):
        self._Stack__push(val)
        print("{} inserted at rear end of Queue".format(val))
    
    
    def deletion(self):
        t = self._Stack__pop()
        if t == 'E':
            return t
        else:
            pop_val = self.deletion()
            if pop_val == 'E':
                pop_val = t
                print("{} deleted from front end of Queue".format(pop_val))
            else:
                self._Stack__push(t)
        
        return pop_val
                
    
    def queSize(self):
        return self.getSize()



if __name__ == "__main__":
    q = Queue()
    q.insertion(3)
    q.insertion(4)
    q.insertion(5)
    print("\nAfter Insertion")
    print("Current Sate of Queue -> ", q, "\n")
    q.deletion()
    q.deletion()
    print("\nAfter Deletion of 3 elements")
    print("Current Sate of Queue -> ", q, "\n")