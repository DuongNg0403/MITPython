class Dogs(object):
        def __init__(self,name,age):
                self.name = name
                self.age = age

        def description(self):
                return "{} is {} years old".format(self.name,self.age)

        def sound(self, sound):
                return "{}".format(sound)
        
class Chihuahua(Dogs):                          #Chihuahua inherits from Dogs
        def personality(self,behavior):
                return "{} is {}".format(self.name, behavior)

mikeisnotadog = Chihuahua("Not Mike", 18)
print(mikeisnotadog.description())
print(mikeisnotadog.personality("Agressive"))