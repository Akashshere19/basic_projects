
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
S
      print("To see")

class Movie( Video,Audio):

 
    def use(self):

       super().use()

m1 = Movie()
m1.use()







class a:
    def f1(self):
        self.name = "S"
        
class b(a):
    pass
        
     
obj=b()
print(b.f1())




















