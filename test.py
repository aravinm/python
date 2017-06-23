# a = [n **2 for n in range(10) if n% 2==0]
# print(a)


# a = "Today is a rainny day"

# c = [i[0] for i in a.split() if 'a' in i and len(i)>3 ]
# print(c)


# a = {i:i*i for i in range(1,11) if i%2 ==0}
# print(a)



# def f(i):
# 	return i*i

# a = [f(i) for i in range(20000000000) if i%3!=0 and i%5!=0]
# # print(a)

# a = (n*n for n in range (10000000000000000000000000000000000))
# for i in a:
# 	print(i)



# namelist = ['Ally','Jane','Belinda']

# a=(i.upper() for i in namelist)

# for n in a:
# 	print(n)


# def even_no(n):
# 	for i in range(n):
# 		if i%2 ==0:
# 			yield i

# a = even_no(1000)
# for i in a:
# 	print(i)

# def fibo():
# 	a,b = 0,1
# 	while True:
# 		yield a
# 		a,b=b,a+b

# f = fibo()



# count = 0
# for i in f:
# 	if( count < 10000):
# 		print(i)
# 	else:
# 		break
# 	count += 1
# 	break

# class Person():
# 	def __init__(self,name,age,ID):
# 		self.n=name
# 		self.a=age
# 		self.i=ID


# 	def is_old(self):
# 		return self.a


# 	def ChangeName(self, newName):
# 		self.n=newName
# 		return self.n

# class Student(Person):
# 	def __init__(self,name,gender,branch,year):
# 		super().__init__(name,gender)
# 		self.b=branch
# 		self.y=year
# s1 Student("Aravin","m","sadads",1997)
# print(s1.name)

# p1 = Person("Tim",15,1111)

# print(p1.is_old())
# p1.ChangeName("James")
# print(p1.n)


# class Rectangle():
# 	def __init__(self,length,width):
# 		self.l=length
# 		self.w=width

# 	def computeArea(self):
# 		 return self.l*self.w


# r1 = Rectangle(23,5)
# print("The total area is",r1.computeArea())

# class Square(Rectangle):
# 	def __init__(self,length):
# 		super().__init__(length,length)



# s1 = Square(Rectangle)
# print(s1.computeArea())
# def perimeter(self):
# 	print("Perimeter = {}".format(4*self.length))


# class Employee():
# 	count=0
# 	def __init__(self,name,salary=0):

# 		self.n=name
# 		self.s=salary

# 		Employee.count+=1

# 	def display(self):
# 		return self.n+","+str(self.s)

# e1 = Employee("Aravin","54.78")
# print(e1.display())
# e2 = Employee("John","100")
# print(e2.display())
# e3 = Employee("adadsda","98")
# print(e3.display())

# print(Employee.count)


# class FullTimeStaff(Employee):
# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		self.l=leave

# 	def display(self):
# 		return self.n+","+str(self.s)+","+self.l


# class PartTimeStaff(Employee):
# 	def __init__(self,name,hourly):
# 		super().__init__(name,salary=0)
# 		self.h=hourly
# 	def display(self):
# 		return self.n+","+ self.h


# ft = FullTimeStaff ("Wee","56.90","234324")

# print(ft.display())

# pt = PartTimeStaff ("Cheong","2.90")
# print(pt.display())


# import sqlite3
# db = sqlite3.connect("test.db")
# # db.commit()


# #Creating of table
# # db.execute("CREATE TABLE student (name text, rank int)")
# db.commit()

# db.execute('insert into student(name,rank) values(?,?)',('Jim',1))
# db.execute('insert into student(name,rank) values(?,?)',('John',2))
# db.execute('insert into student(name,rank) values(?,?)',('Tim',3))
# db.commit()

# a = db.execute('SELECT * FROM student ORDER BY rank')
# db.commit()
# for i in a:
# 	print(i[0]+","+str(i[1]))

# #UPDATE
# db.execute('UPDATE student SET name= ? WHERE rank = ? ',('Tim',2))
# db.commit()

# DELETE
# db.execute('DELETE FROM student WHERE rank=2')
# db.commit()
import sqlite3

db = sqlite3.connect("subject.db")
# db.commit()


# SUBJECTS ADDING OF DATA
# db.execute("CREATE TABLE subjects (subjects text, students text, classes text)")
# db.commit()

# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('English',200,10))
# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('Chinese',50,8))
# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('Math',80,12))
# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('Science',80,12))

# db.commit()

# a = db.execute('SELECT * FROM subjects ORDER BY classes')
# db.commit()
#
# for i in a:
#     print(str(i[0]) + "," + str(i[1]) + "," + str(i[2]))



givenNum = 10# a = [n **2 for n in range(10) if n% 2==0]
# print(a)


# a = "Today is a rainny day"

# c = [i[0] for i in a.split() if 'a' in i and len(i)>3 ]
# print(c)


# a = {i:i*i for i in range(1,11) if i%2 ==0}
# print(a)



# def f(i):
# 	return i*i

# a = [f(i) for i in range(20000000000) if i%3!=0 and i%5!=0]
# # print(a)

# a = (n*n for n in range (10000000000000000000000000000000000))
# for i in a:
# 	print(i)



# namelist = ['Ally','Jane','Belinda']

# a=(i.upper() for i in namelist)

# for n in a:
# 	print(n)


# def even_no(n):
# 	for i in range(n):
# 		if i%2 ==0:
# 			yield i

# a = even_no(1000)
# for i in a:
# 	print(i)

# def fibo():
# 	a,b = 0,1
# 	while True:
# 		yield a
# 		a,b=b,a+b

# f = fibo()



# count = 0
# for i in f:
# 	if( count < 10000):
# 		print(i)
# 	else:
# 		break
# 	count += 1
# 	break

# class Person():
# 	def __init__(self,name,age,ID):
# 		self.n=name
# 		self.a=age
# 		self.i=ID


# 	def is_old(self):
# 		return self.a


# 	def ChangeName(self, newName):
# 		self.n=newName
# 		return self.n

# class Student(Person):
# 	def __init__(self,name,gender,branch,year):
# 		super().__init__(name,gender)
# 		self.b=branch
# 		self.y=year
# s1 Student("Aravin","m","sadads",1997)
# print(s1.name)

# p1 = Person("Tim",15,1111)

# print(p1.is_old())
# p1.ChangeName("James")
# print(p1.n)


# class Rectangle():
# 	def __init__(self,length,width):
# 		self.l=length
# 		self.w=width

# 	def computeArea(self):
# 		 return self.l*self.w


# r1 = Rectangle(23,5)
# print("The total area is",r1.computeArea())

# class Square(Rectangle):
# 	def __init__(self,length):
# 		super().__init__(length,length)



# s1 = Square(Rectangle)
# print(s1.computeArea())
# def perimeter(self):
# 	print("Perimeter = {}".format(4*self.length))


# class Employee():
# 	count=0
# 	def __init__(self,name,salary=0):

# 		self.n=name
# 		self.s=salary

# 		Employee.count+=1

# 	def display(self):
# 		return self.n+","+str(self.s)

# e1 = Employee("Aravin","54.78")
# print(e1.display())
# e2 = Employee("John","100")
# print(e2.display())
# e3 = Employee("adadsda","98")
# print(e3.display())

# print(Employee.count)


# class FullTimeStaff(Employee):
# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		self.l=leave

# 	def display(self):
# 		return self.n+","+str(self.s)+","+self.l


# class PartTimeStaff(Employee):
# 	def __init__(self,name,hourly):
# 		super().__init__(name,salary=0)
# 		self.h=hourly
# 	def display(self):
# 		return self.n+","+ self.h


# ft = FullTimeStaff ("Wee","56.90","234324")

# print(ft.display())

# pt = PartTimeStaff ("Cheong","2.90")
# print(pt.display())


# import sqlite3
# db = sqlite3.connect("test.db")
# # db.commit()


# #Creating of table
# # db.execute("CREATE TABLE student (name text, rank int)")
# db.commit()

# db.execute('insert into student(name,rank) values(?,?)',('Jim',1))
# db.execute('insert into student(name,rank) values(?,?)',('John',2))
# db.execute('insert into student(name,rank) values(?,?)',('Tim',3))
# db.commit()

# a = db.execute('SELECT * FROM student ORDER BY rank')
# db.commit()
# for i in a:
# 	print(i[0]+","+str(i[1]))

# #UPDATE
# db.execute('UPDATE student SET name= ? WHERE rank = ? ',('Tim',2))
# db.commit()

# DELETE
# db.execute('DELETE FROM student WHERE rank=2')
# db.commit()
import sqlite3

db = sqlite3.connect("subject.db")
# db.commit()


# SUBJECTS ADDING OF DATA
# db.execute("CREATE TABLE subjects (subjects text, students text, classes text)")
# db.commit()

# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('English',200,10))
# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('Chinese',50,8))
# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('Math',80,12))
# db.execute('insert into subjects(subjects,students,classes) values(?,?,?)',('Science',80,12))

# db.commit()

# a = db.execute('SELECT * FROM subjects ORDER BY classes')
# db.commit()
#
# for i in a:
#     print(str(i[0]) + "," + str(i[1]) + "," + str(i[2]))



givenNum = 10