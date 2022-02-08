class Student:
    def __init__(self, student_name, marks):
        self.student_name=student_name
        self.marks=marks

    def set_studentName(self, studentName):
        self.student_name=studentName

    def get_student_name(self):
        return self.student_name

    def set_marks(self, marks):
        self.marks=marks

    def get_marks(self):
        return self.marks


def main():

    student1=Student(student_name="mary jane",marks= 92)
    print(student1.student_name, student1.marks)



    student2=Student(student_name="motun", marks=90)
    print(student2.student_name, student2.marks)

    print(student1.get_student_name())

main()