mark = float(input("Enter your marks: "))
if mark >= 85:
    print("Grade: A+")
    print("Excellent!")
elif mark >=80 and mark < 85:
    print("Grade: A")
    print("Well done.")
elif mark >= 75 and mark < 80:
    print("Grade: B+")
elif mark >= 70 and mark < 75:
    print("Grade: B")
elif mark >= 65 and mark < 70:
    print("Grade: C+")
elif mark >=60 and mark < 65:
    print("Grade: C")
elif mark >=55 and mark < 60:
    print("Grade: D+")
elif mark >=50 and mark < 55:
    print("Grade: D")
else:
    print("Grade: F\nSee me.")
