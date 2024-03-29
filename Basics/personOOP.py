import datetime
class Person(object):
        def __init__(self, name):
                """Create a person"""
                self.name = name
                try:
                        lastBlank = name.rindex(' ')
                        self.lastName = name[lastBlank+1:]
                except:
                        self.lastName = name
                self.birthday = None
        def getName(self):
                """Returns self's full name"""
                return self.name
        def getLastName(self):
                """Returns self's last name"""
                return self.lastName
        def setBirthday(self, birthdate):
                """Assumes birthdate is of type datetime.date
                Sets self's birthday to birthdate"""
                self.birthday = birthdate
        def getAge(self):
                """Returns self's current age in days"""
                if self.birthday == None:
                        raise ValueError
                return (datetime.date.today() - self.birthday).days
        def __lt__(self, other):
                """Returns True if self's name is lexicographically
                less than other's name, and False otherwise"""
                if self.lastName == other.lastName:
                        return self.name < other.name
                return self.lastName < other.lastName
        def __str__(self):
                """Returns self's name"""
                return self.name

class MITPerson(Person):
        nextIdNum = 0 #identification number
        def __init__(self, name):   #this line overrides the inheritance 
                Person.__init__(self, name) #this line keeps the inheritance
                self.idNum = MITPerson.nextIdNum
                MITPerson.nextIdNum += 1
        def getIdNum(self):
                return self.idNum
        def __lt__(self, other):
                return self.idNum < other.idNum
'''
mike = Person("Mike Nguyen")
fullName = mike.getName()
lastName = mike.getLastName()
mike.setBirthday(datetime.date(2001,5,25))
age = mike.getAge()
print("I am {}, my last name is {}, I am {} days old".format(fullName,lastName,age))
james = Person("James Bond")

print(james.lastName > mike.lastName)'''
p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

#print(p4<p1) # short hand for p4.__lt__(p1)
#p1<p4 will raise an exception error because p1__lt__(p4)
#print(p1<p4) 
### make good use of isinstance(object, class or tuple)
class Student(MITPerson):
    pass
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
class Grad(Student):
    pass

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    def getGrades(self, student):
        """Return a list of grades for student"""
        try: #return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
    def getStudents(self):
        """Return the students in the grade book one at a time"""
#        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] #return copy of list of students
#        for s in self.students: #generator
#            yield s
def gradeReport(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n' + str(s) + '\'s mean grade is ' + str(average) #look at that "\'"
        except ZeroDivisionError:
            report = report + '\n' + str(s) + ' has no grades'
    return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)
sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))
for stu in sixHundred.getStudents():
    print(stu)
book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
    print (s)