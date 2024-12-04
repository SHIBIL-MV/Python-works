class GrandParents:

    def m1(self):

        print("grand parent class m1 method")

class Parents():

    def m2(self):

        print("parent class m2 methods")

class Child(Parents,GrandParents):

    def m3(self):

        print("child class m3")

child_inheritance=Child()

child_inheritance.m3()

child_inheritance.m2()

child_inheritance.m1()