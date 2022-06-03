#Mia Escoto
#Student Database


student_database = {
   'first_name' : [],
   'last_name' : [],
   'student_id' : [],
   'grade_in_school' : [],
   'grade_in_class' : [],
}

lastName = student_database["last_name"] 
firstName = student_database["first_name"]
studentID = student_database["student_id"]
gradeInSchool = student_database["grade_in_school"]
gradeInClass = student_database["grade_in_class"] 
def showMenu():
   print("\nWelcome to the student database!")
   while True: 
      try: 
         user_function = int(input("""please enter the number of what you would like to do.
1. Add student information
2. Delete student information
3. Display student information by grade year
4. Display student information by grade and class
5. Display students whose last name start by any letter
6. Display all students
7. Exit the student information management system
: """))
         if user_function not in range(1, 8):
            print("*Please enter a number 1-7*\nre enter form:")
            continue 
         break
      except ValueError:
         print("Please enter a NUMBER")
   print()
   return user_function

grades = ['A', 'B', 'C', 'D', 'F']
year = ['9', '10', '11', '12',]


def add_stud():
   while True: 
      first_name = input("First name of student: ").lower().strip()
      if first_name == "":
         print("Please enter a first name")
         continue
      break
   while True:
      last_name = input("Last name of student: ").lower().strip()
      if last_name == "":
         print("Please enter a last name")
         continue
      break
   if last_name in lastName:
      while True:
         try:
            nameCheck = int(input("\nsomeone with this last name is alrady in the database are you sure you want to add them?\n1 for yes, any other number if not: "))
            if nameCheck == 1: 
               break
            else:
               print("Student not added")
               return False
         except ValueError:
            print("Please enter a number")
   student_id = 1
   for i in range(len(studentID)):
      if studentID[i] == student_id:
         student_id +=1
      if student_id in studentID:
         student_id +=1
   while True: 
      grade_in_school = input("Student year in school: ")
      if grade_in_school not in year:
         print("*please enter the correct grade year: 9, 10, 11, or 12 \nRe enter form:*")
         continue
      break
   while True: 
      grade_in_class = input("Student class grade: ").upper().strip()
      if grade_in_class not in grades:
         print("*please enter the correct grades: A, B, C, D, or F *\nRe enter form:")
         continue
      break
   while True:
      try:
         confirmation = int(input("Are you sure you would like to add this student?\n 1 for yes, any number for no: "))
         if confirmation == 1:
               firstName.append(first_name)
               lastName.append(last_name)
               studentID.append(student_id)
               gradeInSchool.append(grade_in_school)
               gradeInClass.append(grade_in_class)
               print("Student Added.")
               break
         else:
            print("student NOT added")
            break
      except ValueError:
         print("Please enter a number 1 or 0")
         continue
      break


def del_stud():
   if len(studentID) == 0:
      print("Database is currently empty")
   else: 
      while True:
         last_name = input("Last name of student: ").lower()
         if last_name not in lastName:
            print("This last name is not in the database")
            continue
         for i in range(len(lastName)):
            if lastName[i] == last_name:
               print(f"{lastName[i]}, {firstName[i]}, id: {studentID[i]}")
         break
      while True:
         try: 
            student_id = int(input("Please enter the ID of the student you would like to remove: "))
            if student_id not in studentID:
               print("*this ID is not in our database*\nplease enter a new ID:")
               continue
            break
         except ValueError: 
            print("*Please enter the correct value*")
      for i in range(len(studentID)):
         if studentID[i] == student_id:
            del(studentID[i])
            del(lastName[i])
            del(gradeInSchool[i])
            del(gradeInClass[i])
            del(firstName[i])
            break
      print("Student Removed.")

def find_byLast():
   if len(studentID) == 0:
      print("Database is currently empty")
   else:
      while True:
         last_letter = input("Please enter the letter of the last names of the students: ").lower()
         if len(last_letter) != 1 or ord(last_letter) not in range(96, 122): 
            print("*Please enter one letter*\nRe enter letter:")
            continue
         break
      print(f"The following students last name start with {last_letter}: ")
      for i in range(len(lastName)):
         if lastName[i][0] == last_letter:
            print(lastName[i], firstName[i])

def find_by_gradeYear():
   if len(studentID) == 0:
      print("Database is currently empty")
   else:
      while True:
         grade_in_school = input("Student year in school: ")
         if grade_in_school not in year:
            print("*please enter the correct grade year: 9, 10, 11, or 12 \nRe enter form:*")
            continue
         if grade_in_school not in gradeInSchool:
            print("There are no students in this grade.")
            break
         break
      for i in range(len(gradeInSchool)):
         if gradeInSchool[i] == grade_in_school:
            print(f"{firstName[i]} {lastName[i]}, {gradeInSchool[i]}th grade")

def find_by_gradeS():
   if len(studentID) == 0:
      print("Database is currently empty")
   else:
      while True: 
         try: 
            grade_in_school = input("Student year in school: ")
            if grade_in_school not in year:
               print("*please enter the correct grade year: 9, 10, 11, or 12 \nRe enter form:*")
               continue
            grade_in_class = input("Student class grade: ").upper().strip()
            if grade_in_class.upper() not in grades:
               print("*please enter the correct grades: A, B, C, D, or F *\nRe enter form:")
               continue
            break
         except ValueError:
            print("*Please enter correct value*\nRe enter form:")
      for i in range(len(gradeInSchool)):
         if gradeInSchool[i] == grade_in_school and gradeInClass[i] == grade_in_class:
            print(f"{firstName[i]} {lastName[i]}, {gradeInSchool[i]}th grade, grade: {gradeInClass[i]}")
            #When there is no one 1/value 

def showAll():
   if len(studentID) == 0:
      print("Database currently empty")
   else:
      for i in range(len(lastName)):
         print (f"student: {firstName[i]} {lastName[i]}, ID: {studentID[i]}, {gradeInSchool[i]}th grade, grade: {gradeInClass[i].upper()}")

while True: 
   user_function = showMenu()
   if user_function ==  1:
      add_stud()
   if user_function == 2: 
      del_stud()
   if user_function == 3: 
      find_by_gradeYear()
   if user_function == 4: 
      find_by_gradeS()
   if user_function == 5: 
      find_byLast()
   if user_function == 6: 
      showAll()
   if user_function == 7: 
      print("Goodbye") 
      break  