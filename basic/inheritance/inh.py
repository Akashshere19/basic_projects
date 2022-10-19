"""
#Duck Typing
class Laptop:
    def execute(self):
        print("compiling")
        print("running")

class Computer:
    def execute(self):
        print("feature")
        print("feature2")
        
        print("compiling")
        print("running")

class MyEditor:
    def code(self,ide):
        print("class")
        ide.execute()

        
ide=Computer()

lap1 = MyEditor()

lap1.code(ide) """

"""
#Duck Typing
class A:
    def exe(self):
        print("execute1")

class B:
    def exe(self):
        print("execute2")


class C:
    def exe2(self,ide):
        ide.exe()
       


for obj in A(),B(),C():
    obj.exe() """


"""
class VisualStudio:  
     def execute(self):  
         print('Compiling')  
         print('Running')  
         print('Spell Check')  
         print('Convention Check')


           
class Desktop:  
    def code(self, ide):  
        ide.execute()  
  
  
ide  = VisualStudio()         
desk = Desktop()  
desk.code(ide) """

"""
class Duck:  
   def swim(self):  
         print("I'm a duck, and I can swim.")  
   
class Sparrow:  
     def swim(self):  
         print("I'm a sparrow, and I can swim.")  
   
class Crocodile:  
     def swim_walk(self):  
         print("I'm a Crocodile, and I can swim, but not quack.")  
   
def duck_testing(animal):  
     animal.swim()  
       
       
duck_testing(Duck())  
duck_testing(Sparrow())  
duck_testing(Crocodile())  """

"""
class A:
    def execute(self):
        print("hi")
class B:        
    def execute(self):
        print("akash")
class C:        
    def execute(self):
        print("how are you..?")
class D:
    def exe(self,ide):
        ide.execute()


for obj in A(),B(),C():
    obj.execute() 


idi=D()
ide = A()
idi.exe(ide) """



