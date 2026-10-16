
name = input("Enter your name: ")
marks = float(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")
