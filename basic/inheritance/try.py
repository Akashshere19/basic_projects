
"""
class A:
    def feature1(self):
        print("feature 1")
class B:
    def feature2(self):
        print("feature 2")
obj=B()
obj.feature2()"""

"""
#Single Inheritance
class A:
    def feature1(self):
        print("feature 1")
    def feature2(self):
        print("feature 2")

class B(A):
    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature4")

obj=B()

obj.feature1()

obj1 =A()
obj.feature3()"""

"""
#multilevel inheritance
class A:
    def feature1(self):
        print("feature1")
class B(A):
    def feature2(self):
        print("feature2")

class C(B):
    def feature3(self):
        print("feature3")

class D(C):
    def feature4(self):
        print("feature4")

obj=C()
obj.feature1()

obj1=D()
obj1.feature4()
obj1.feature2()  """

"""
#Multiple Inheritance
class A:
    def feature1(self):
        print("feature1")
        
    def fetaure2(self):
        print("feature2")

class B:
    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")
class C:
    def feature5(self):
        print("feature5")
class D(A,B,C):
    def feature6(self):
        print("feature6")        

obj = D()
obj.feature1() """

"""
#Hierichial Inheritance

class A:
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
class B(A):
    def feature3(self):
        print("feature3")
class C(A):
    def feature4(self):
        print("feature4")
        
obj = C()
obj.feature1()"""

"""
#Hybrid inheritance
class A:
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
class B:
    def feature3(self):
        print("feature3")
class C(A):
    def feature4(self):
        print("feature4")

class D(C,B):
    def feature4(self):
        print("feature4")        
obj = C()
obj.feature3() """
        
