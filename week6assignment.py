def log_action(func):
    def wrapper(*args,**kwargs):
        print(f"[ACTION] {func.__name__} executed")
        result=func(*args, **kwargs)
        return result
    return wrapper


class Student:
    _total_students=0
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id 
        self._courses={}
        Student._total_students+=1

    @log_action
    def enroll(self,course_code,grade):
        upper_cased=course_code.upper()
        self._courses[upper_cased]=grade
        return (f"{self.name} enrolled in {course_code} with grade {grade}")
    
    def gpa(self):
        total=0
        for grade in self._courses.values():
            total+=grade
        if len(self._courses)==0:
            return 0.0
        return round(total/len(self._courses), 1)
    
    def best_course(self):
        if len(self._courses)==0:
            return "No courses"
        
        perfect_course=None
        perfect_grade=0
        for course,grade in self._courses.items():
            if perfect_grade < grade:
                perfect_grade=grade
                perfect_course=course
        return perfect_course
    
    @classmethod
    def from_registration(cls,data):
        name,student_id=data.split("-")
        return cls(name,student_id)
        
    @staticmethod
    def is_valid_id(student_id):
        if len(student_id) ==7:
            return True
        else:
            return False
        
    @classmethod
    def total_students(cls):
        return cls._total_students


s1 = Student("Aziza", "2601001")
s1.enroll("math101", 85)
s1.enroll("phys201", 92)
s1.enroll("eng102", 78)

s2 = Student.from_registration("Jasur-2601002")
s2.enroll("CS101", 95)
s2.enroll("math101", 88)

print(f"{s1.name}: GPA = {s1.gpa()}, Best = {s1.best_course()}")
print(f"{s2.name}: GPA = {s2.gpa()}, Best = {s2.best_course()}")

print(f"Valid ID '2601001': {Student.is_valid_id('2601001')}")
print(f"Valid ID '26A': {Student.is_valid_id('26A')}")
print(f"Total students: {Student.total_students()}")


        

    
    