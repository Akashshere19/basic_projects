"""class A:
    def __init__(self): #constructor
        print("Init A")
        
    def feature1(self):
        print("feature 1")
        
class B:
    def __init__(self):
        super().__init__() #for take init of class A
        super().feature1() #for take feature1 
        print("Init B")
        
    def feature2(self):
        print("feature 2")

class C(A,B):
    def __init__(self): #MRO(Method Resolution Method) use only in multiple inheritance
        super().__init__()
        print("Init C")

        
a1=C()

a1.feature2()  """

# Super example
class Fruit:
    def taste(self):
        str = "Sweet"
        return str
class Lemon(Fruit):
    def taste(self):
        str = "Sour"
        return   super().taste()
     
        
lemon1 = Lemon()
print(lemon1.taste())

#super
class Audio:

    def use(self):

       print("To listen")

class Video:

    def use(self):

      print("To see")

class Movie( Video,Audio):

 
    def use(self):

       super().use()

m1 = Movie()
m1.use()
