class evcennumbers :
    def __init__(self , start , end ) :
        self.start = start 
        self.end = end 
    def __iter__ (self):
        self.current = self.start 
        if self.current % 2 != 0 :
            self.current += 1 
        return self 
    def __next__(self):
        if self.current >self.end :
            raise StopIteration 
        num = self.current 
        self.current +=2 
        return num 
    
even_nums = evcennumbers(1 , 10 )
for n in even_nums :
    print (n)