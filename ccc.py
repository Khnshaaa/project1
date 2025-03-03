class worditerator :
    def __init__(self , word) :
        self.word = word 
        
    def __iter__(self):
        self.index = 0 
        return self
    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration 
        letter = self.word [self.index]
        self.index += 1
        return letter 

word = worditerator("puthon and c++")

for letter in word :
    print(letter)