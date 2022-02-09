class StudentB:

    def __init__(self,student_name,  student_id):
        self.student_id=student_id
        self.student_name=student_name
        self.student_class="B"
        self.student_name='tolu'
    # def set_student_name(self, studentName):
    #     self.student_name=studentName
    def get_student_name(self):
        return self.student_name
    def set_student_id(self, student_id):
        self.student_id=student_id
    def get_student_id(self):
        return self.student_id
    def get_student_class(self):
        return self.student_class

def main():
    student=StudentB(student_name='tolu', student_id='890')
    # student.__delattr__()
    print(student.__dict__)
    student.__delattr__(student)
    print(student.__dict__)
    # student_b=StudentB( student_id=111)
    # print(student_b.get_student_name(), student_b.get_student_id(), student_b.get_student_class())
    # student_b=StudentB(student_id=90)
    # print(student_b.get_student_id(), student_b.get_student_class())



main()