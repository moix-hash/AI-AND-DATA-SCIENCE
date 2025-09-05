students = []
def add_students():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    subject = input("Enter subject: ")
    marks = int(input("Enter marks: "))
    students.append([name, roll ,subject,marks])
    print("Students added sucessfully")
    
def display_students():
    if not students:
        print("No student found")
        return 
    print ("Student Details:") 
    for student in students:
        print(f"Name: {student[0]},Roll No:{student[1]},Subject:{student[2]},Marks:{student[3]}")
def search_students():
    roll = input("Enter roll number to search: ")
    for student in students:
        if student[1] == roll:
            print(f"Name: {student[0]},Roll No: {student[1]},subject:{student[2]},Marks:{student[3]}")
            return 
        print ("Student not found")
def update_students():
    roll = input("Enter the roll number of the student to update :")
    for student in students:
        if student[1] == roll:
             new_marks = int(input("Enter new marks: "))
             student[3] = new_marks
             print(" Marks updated successfully!\n")
             return
    print(" Student not found!\n")
def delete_students():
      roll = input("Enter roll number to delete: ")
      for student in students:
        if student[1] == roll:
            students.remove(student)
            print(" Record deleted successfully!\n")
            return
      print("⚠️ Student not found!\n")         
def sort_students():
    if not students:
        print("⚠️ No records to sort!\n")
        return
    students.sort(key=lambda x: x[3], reverse=True)
    print(" Records sorted by marks (descending order)!\n")
while True:
    print("===== SRMS (Nested List) =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Sort Students by Marks")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_students()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_students()
    elif choice == '4':
        update_students()
    elif choice == '5':
        delete_students()
    elif choice == '6':
        sort_students()
    elif choice == '7':
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice! Try again.\n")                       
        
        