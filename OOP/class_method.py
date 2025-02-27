class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 3.4)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_avg_gpa())