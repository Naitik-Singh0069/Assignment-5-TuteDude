student_marks = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 92,
    "Eve": 88
}

name = input("Enter the student's name: ")

marks = student_marks.get(name)
if marks is not None:
    print(f"{name}'s marks: {marks}")
else:
    print(f"Student '{name}' not found in the records.")