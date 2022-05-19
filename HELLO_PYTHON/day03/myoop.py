class Animal:
    
    def __init__(self,myage):
        print("생성자",myage)
        self.mylife = 100
        self.myage = myage
        
    def getAge(self):
        self.myage += 1
        self.mylife -= 1
    def __del__(self):
        print("소멸자",self.myage)
        
        
print("myoop",__name__)
        
if __name__ == '__main__':
    ani = Animal(5)
    

