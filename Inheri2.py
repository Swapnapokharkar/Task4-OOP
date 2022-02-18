class Parent:
  def f1(self):
    print("Function of parent class.")

class Child_1(Parent):
  def f2(self):
    print("Function of child_1 class.")

class Child_2(Child_1):
  def f3(self):
    print("Function of child_2 class.")

obj_1 = Child_1()
obj_2 = Child_2()
obj_1.f1()
obj_1.f2()

print("\n")
obj_2.f1()
obj_2.f2()
obj_2.f3()