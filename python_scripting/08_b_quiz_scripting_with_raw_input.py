names =  input("Enter Students name (Separated by commas): ")
assignments = input("Enter Missing assignments numbers (Separated by commas): ")
grades = input("Enter grades, obtained by student (Separated by commas): ")

names_list = names.split(",")
assignments_list = assignments.split(",")
grades_list = grades.split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date\
.\n\n"

if (len(names_list) == len(assignments_list) and len(assignments_list) == len(grades_list)):
    for name, assignment, grade in zip(names_list, assignments_list, grades_list):
        print(message.format(name, assignment, grade, int(grade) + 2*int(assignment)))
