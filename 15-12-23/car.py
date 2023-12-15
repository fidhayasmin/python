class A:
    def __init__(self,color,price,kilometer):
        self.color=color
        self.price=price
        self.kilometer=kilometer
        
    def __gt__(self,price):
        if(self.price<other.price):
            return True
        else:
            return False
        obj1=car(20000)
        obj2=car(10000)
        if(obj1>obj2):
            print("object1 is greater than object2")
        else:
            print("object2 is greater than object1")
            
            
