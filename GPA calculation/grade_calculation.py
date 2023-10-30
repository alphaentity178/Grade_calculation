# Develop a GPA Calculator using Python...........

def grade_calculation(marks , sub) :
    marks = int(marks)
    if (91 <= marks <= 100) :
        print("Your {} grade is : A+".format(sub))
    elif (81 <= marks <= 90) :
        print("Your {} grade is : A".format(sub))
    elif (71 <= marks <= 80) :
        print("Your {} grade is : B".format(sub))
    elif (61 <= marks <= 70) :
        print("Your {} grade is : C".format(sub))
    elif (41 <= marks <= 60) :
        print("Your {} grade is : D".format(sub))
    elif (0 <= marks <= 40) :
        print("Your {} grade is : F".format(sub))

bangla = input("Enter your Bangla sub's marks : ")
english = input("Enter your English sub's marks : ")
math = input("Enter your Math sub's marks : ")
science = input("Enter your Science sub's marks : ")
bng = "Bangla"
eng = "English"
mat = "Math"
sce = "Science"

grade_calculation(bangla , bng)
grade_calculation(english , eng)
grade_calculation(math , mat)
grade_calculation(science , sce)
