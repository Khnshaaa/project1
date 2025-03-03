class numbers :
    def __init__(self , start , end ):
        self.start = start 
        self.end = end 
        
    def __iter__(self):
        self.current = self.start 
        return self 
    def __next__(self):
        if self.current > self.end :
            raise StopIteration 
        number = self.current
        self.current += 1 
        return number 
nums = numbers ( 1 , 5 ) 
iterator = iter(nums)

for  num in iterator :
    print (num)
    
