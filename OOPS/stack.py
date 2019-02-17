class Stack(object):
    def __init__(self):
        self.__st = []
        self.__top = -1
    
                    
    def __isEmpty(self):
        if self.__top == -1:
            return True
        else:
            return False
    
    
    def getSize(self):
        return self.__top+1
    
    
    def __push(self, x):
        self.__st.append(x)
        self.__top += 1
    
    def __pop(self):
        if self.__isEmpty():
            return 'E' #empty Stack
        else:
            x = self.__st[self.__top]
            del self.__st[self.__top]
            self.__top -= 1
            return x
            
    def __repr__(self):
        return str(self.__st)
    
    #called only when scope of stack object is over
    def __del__(self):
        print("deleting stack")
        
