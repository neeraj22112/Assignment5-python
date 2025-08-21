stud_marks={
    'Neeraj':75,
    'Rahul':85,
    'Nitin':89,
    'Bipul':79,
    'Anurag':92,
    'Rohit':72,
}
name = input("Enter the name of the student: ")
if name in stud_marks:
    print(f"{name}'s marks is:{stud_marks[name]}")
else:

    print(f"{name} named student not found")
