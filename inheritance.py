
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B:

    def __init__(self):
#        super().__init__()          #to call the constructor in super class
        print("In B init")
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

#class C(B):                          # Multi level inheritance(A==B==C)
class C(B,A):                           #multiple inheritance(C==A&B)
    def __init__(self):
        super().__init__()
        print("In C init")
    def feature5(self):
        print("Feature 5 is working")
    def feature6(self):
        print("Feature 6 is working")


# x1=A()
# x1.feature1()
# x1.feature2()


# y1=B()
# y1.feature3()
# y1.feature4()
#y1.feature2()          multilevel inheritance
#y1.feature1()          multilevel inheritance

# z1=C()
# z1.feature3()           #Multiple inheritnce
# z1.feature4()           #Multiple inheritnce
# z1.feature2()           #Multiple inheritnce
# z1.feature1()           #Multiple inheritnce

#Constructor inheritance
#MRO: Method Resolution Order

#x=A()                   #it will print "in A init"

#for class B(A):

z1=C()
#it will print "in A init"
#As B is inheriting the properties of A so constructor is also inherited from the parent class

# when we add constructor in class A and B, if we call from object B then it will consider the constructor in B,
# if constructor is not there in B then it will search from the parent class.

# if i have constructor in class A and B and we want to call both constructor then follow below method:
#   super().__init__()          #to call the constructor in super class

# for class C(A,B):              # C is having 2 super classes
#if we run:
# class C(A,B):                           #multiple inheritance(C==A&B)
#     def __init__(self):
#         super().__init__()
#         print("In C init")
# it will print the constructor of the first class object(Here it is A)

#Here Method resolution order [MRO] come into picture:
#Similarly super method is also multiple inheritance will start from left to right

