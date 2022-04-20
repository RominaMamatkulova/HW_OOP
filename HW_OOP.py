#средние оценки всех студентов по курсу
def calculate_grades_student(list_students, course):
    count = 0
    sum_grade = 0
    av_grade = 0
    for stud in list_students:
        for course1 in stud.courses_in_progress:
            if course1 == course:
                for key, grade in stud.grades.items():
                    if course in key:
                        sum_grade += sum(grade)
                        count += 1
    if count != 0:
        av_grade = sum_grade / count
    return av_grade
#средние оценки лекторов по курсу
def calculate_grades_lector(list_lector, course):
    count = 0
    sum_grade = 0
    av_grade = 0
    for lector in list_lector:
        for course1 in lector.courses_attached:
            if course1 == course:
                for key, grade in lector.grades.items():
                    if course in key:
                        sum_grade += sum(grade)
                        count += len(grade)
    if count != 0:
        av_grade = sum_grade / count
    return av_grade

class Student:
    def __init__(self, name, surname, gender, grade_stud=0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_stud = 0
    #метод выставления оценок лекторам
    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def calc_grade(self):
        count = 0
        sum_grade = 0
        av_grade = 0
        #st_course = ""
        for course in self.courses_in_progress:
            #st_course = f'{st_course}{course},'
            for key, grade in self.grades.items():
                if course in key:
                    sum_grade += sum(grade)
                    count += len(grade)
        av_grade = sum_grade / count
        self.grade_stud = av_grade
        return av_grade
    def __str__(self):
        st_course = ""
        for course in self.courses_in_progress:
            st_course = f'{st_course}{course},'
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.calc_grade()} \nКурсы в процессе изучения: {st_course} \nЗавершенные курсы: Введение в программирование'
        return res
    def __lt__(self, other):
        return self.grade_stud < other.grade_stud

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, grade_lect=0):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.grade_lect = grade_lect
    def calc_grade(self):
        count = 0
        sum_grade = 0
        av_grade = 0
        for course in self.courses_attached:
            for key, grade in self.grades.items():
                if course in key:
                    sum_grade += sum(grade)
                    count += len(grade)
        av_grade = sum_grade / count
        self.grade_lect=av_grade
        return av_grade
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.calc_grade()}'
        return res
    def __lt__(self, other):
        return self.grade_lect < other.grade_lect


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res
#введем проверяющих
some_reviewer = Reviewer('Ivan', 'Petrov')
some_reviewer.courses_attached += ['Java']
some_reviewer.courses_attached += ['Python']

good_reviewer = Reviewer('Irina', 'Kashina')
good_reviewer.courses_attached += ['Python']

#введем лекторов
some_lectorer = Lecturer('Alex', 'Govorun')
some_lectorer.courses_attached += ['PHP']
some_lectorer.courses_attached += ['Java']

good_lectorer = Lecturer('Maksim', 'Chan')
good_lectorer.courses_attached += ['PHP']
good_lectorer.courses_attached += ['Java']
good_lectorer.courses_attached += ['Python']



#введем студентов
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
some_student.courses_in_progress += ['PHP']

good_student = Student('Philipp', 'Rogin', 'your_gender')
good_student.courses_in_progress += ['Python']


#студенты ставят оценки лекторам
some_student.rate_lector(some_lectorer, 'PHP',10)
some_student.rate_lector(some_lectorer, 'PHP',9)
some_student.rate_lector(some_lectorer, 'Java',8)

good_student.rate_lector(good_lectorer, 'Python',10)


#проверяющие оценивают студентов
some_reviewer.rate_hw(some_student, 'Java', 6)
some_reviewer.rate_hw(some_student, 'Python', 8)

good_reviewer.rate_hw(good_student, 'Python', 10)

#print(best_student.grades)
print(some_reviewer.courses_attached)
print(some_lectorer.courses_attached)
print(some_lectorer.grades)
print(some_reviewer)
print(some_lectorer)
print(some_student)
students_list = [good_student, some_student]
print(calculate_grades_student(students_list,'Python'))
lector_list = [good_lectorer, some_lectorer]
print(calculate_grades_lector(lector_list,'PHP'))
#print(good_lectorer.calc_grade())
good_lectorer.calc_grade()
some_lectorer.calc_grade()
some_student.calc_grade()
good_student.calc_grade()
#print(some_student.grade_stud)
print(good_lectorer < some_lectorer)
print(some_student < good_student)
