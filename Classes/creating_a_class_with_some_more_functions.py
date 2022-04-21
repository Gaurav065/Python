from torch import true_divide


class number_ops:
    def __init__(self,number,range_n):
        self.number = number
        self.range_n = range_n
    def digit_chopper(self):
        temp = self.number
        d=0
        while(temp!=0):
            d=temp%10
            temp = temp//10
            print(d)
        return d
    def pallindrome(self):
        temp = self.number
        s=0
        s=s+(digit_chopper(temp)*10)
        if (s==temp):
            return True
        else:
            return False

obj=number_ops(123,0)
obj.digit_chopper()
obj.pallindrome()