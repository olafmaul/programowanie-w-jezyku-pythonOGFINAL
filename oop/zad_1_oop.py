class Student:
   def __init__(self, name, marks):
       self.name = name
       self.marks = marks


   def is_passed(self):
       if not self.marks:
           return False


       average = sum(self.marks) / len(self.marks)
       return average > 50


student1 = Student("Maria Wolska", [22, 33, 80, 90])
print(f"Student {student1.name} zdał? {student1.is_passed()}")


student2 = Student("Mariusz Kanol", [22, 14, 65, 40])
print(f"Student {student2.name} zdał? {student2.is_passed()}")
