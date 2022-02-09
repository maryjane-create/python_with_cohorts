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
    student=Student(student_name="mary jane", marks=9)
    print(student.get_student_name(), student.get_marks())
    student.set_studentName(studentName='motun')
    student.set_marks(90)
    student1name=student.get_student_name()
    student1marks=student.get_marks()
    print(student1name, student1marks)




main()