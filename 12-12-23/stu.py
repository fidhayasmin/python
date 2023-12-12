class student:
    school_name='ABC SCHOOL'
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("Mingyu",27)
print('student:',s1.name,s1.age)
print('school name:',student.school_name)
s1.name="Jun"
s1.age=19
print('studentname:',s1.name,s1.age)
student.school_name='xyz school'
print('schoolname:',student.school_name)
