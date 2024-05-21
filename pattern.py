class Pattern:
    def __init__(self,num):
        self.num=num
    
    #******question 19
    def pattern_one(self):
        for i in range(1,self.num+1):
            for j in range(1,self.num+1):
                print("*",end="")
            print(" ")

    #*********question 20
    def pattern_two(self):
        for i in range(1,self.num+1):
            for j in range(1,i+1):
                print("*",end="")
            print(" ")

    #***** question 21
    def pattern_three(self):
        for i in range(1,self.num+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print(" ")

    
    #******* questionn 22
    def pattern_four(self):
        for i in range(1,self.num+1):
            for j in range(self.num*2,0,-1):
                print("*".center(j),end=(" "))
            print()

obj=Pattern(5)
obj.pattern_one()
obj.pattern_two()
obj.pattern_three()
obj.pattern_four()

