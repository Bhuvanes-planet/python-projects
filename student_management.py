students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        mark = input("Enter Mark: ")

        students.append([name, mark])
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent Records")
        for student in students:
            print("Name:", student[0], "| Mark:", student[1])

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
