class Animal:
    
    def __init__(self):
        self.mylife = 100
        self.myage = 0
        
    def getAge(self):
        self.myage += 1
        self.mylife -= 1

class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.skill_lang = 1
        
    def exp(self,mama):
        self.skill_lang += mama
    
    def getAge(self):
        Animal.getAge(self)
        
if __name__ == '__main__':
    man = Human()
    print(man.mylife)
    print(man.myage)
    print(man.skill_lang)
    man.getAge()
    man.exp(100)    
    print(man.mylife)
    print(man.myage)
    print(man.skill_lang)
    
    
    
    
    
    

