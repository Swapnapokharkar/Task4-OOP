class Parent:
  def f1(self):
    print("Function of parent class.")

class Child(Parent):
  def f2(self):
    print("Function of child class.")

object1 = Child()
object1.f1()
object1.f2()