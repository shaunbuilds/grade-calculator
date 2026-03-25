name = input ("What is your name? ")
grade_book = []
total = 0
while True:
    subject = input("Enter your subject (or type done): ")
    if subject == "done":
        break
    grade = int(input("Enter your grade: "))
    report = {"subj" : subject, "grd" : grade}
    grade_book.append(report)
print(f"{name}'s Grade Book: ")
for grade_books in grade_book:
    print(f"\n {grade_books['subj']} : {grade_books['grd']}")
    total += grade_books['grd']
no_of_subjects = len(grade_book)
average = total/no_of_subjects
print(f"\n{name}'s average is {average}")
if average > 80:
    print("Excellent Work")
elif average > 60 and average <80:
    print("Good Work! Keep it up!")
elif average > 40 and average < 60:
    print("You need to improve, you're barely getting by.")
else:
    print("You have failed.")
