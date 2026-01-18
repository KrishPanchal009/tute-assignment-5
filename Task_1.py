students = {
    "krish": 85,
    "amit": 78,
    "neha": 92,
    "riya": 88
}


name = input("Enter the student's name: ")


for student in students:
    if re.search(name, student):
        print(f"Marks of {name}: {students[student]}")
        break
    else:
        print("Student name not found.")
        break
