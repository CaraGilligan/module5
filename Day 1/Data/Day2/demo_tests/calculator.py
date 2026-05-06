class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b
    
    def get_subtract(self):
        return self.a - self.b
    
    def get_multiply(self):
        return self.a * self.b
    
    def get_divide(self):
        return self.a / self.b

##best practice - put what you're doing in the code under this function 
if __name__ == "__main__" : 
    myCalc = calculator(a=3,b=5)
    print(myCalc.get_sum)