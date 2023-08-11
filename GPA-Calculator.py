from tabulate import tabulate       ##Using it to form table
##intilazing:
totalch=0
gpa=0

## Arrays
z=[]
engrades=[]
mycourse=[]
credit=[]
grades=['A','B+','B','C+','C','D+','D','F']               ##Grades
gradesnum=[4,3.5,3,2.5,2,1.5,1,0]                     ##Grades point
## Starting code:

print("Do you want to calculate GPA?")
dec=str(input("Yes/No:   "))                       ##Giving user the right to decide what to do
if dec=="yes" or dec=="Yes" or dec=="YES":                       ##If yes is entered then gpa calculator will work
    ###display table
    storeddata = {"":[1,2,3,4,5,6,7,8],"Grades":grades,  "Credit points":gradesnum}
    col_names1 = ["","Grades", "Credit"]                                                         ##define header names
    print(tabulate(storeddata, headers=col_names1, tablefmt="fancy_grid"))   ##Printing arrays in table form for user to understand grades and their credit value
    y=int(input("Please enter a number of courses: "))                                       ##taking the number of courses 
    if y>0:         ## To check whether the entered number of courses is >0 or not.
        f=1
        while y>0:                                ##y=counter (Number of courses entered by user )
            gpas=0
            mycourse.append(input("Enter course name: " ))                 ##saving course names in mycourse array
            cr=int(input("Enter credit hours: " ))                      ##Taking credit hours as input from user
            credit.append(cr)                                           ##Saving credit hours of courses in credit array
            z.append(f)                           ##Use as index for table of input table
            f=f+1
            if cr<=0:
                print("Incorrect Credit hours")                       ##Telling user if he has enter incorrect credit hours 
                break                                           ##leaving the while loop if credit hours<=0
            eng=(str(input("Enter grade: ")))                  ##Saving grades of courses
            engrades.append(eng)
            if eng in grades:
                c=(grades.index(eng,0,8))
                d=gradesnum[c]
                gpas=(cr*d)                             ##gpas=Individual gpa of course 
                totalch=totalch+cr                      ##Sum of credits entered is stored in totalch
            else:
                print("Incorrect grade entered")        ##Telling user if he has enter incorrect grades 
                break
            gpa=gpa+gpas                       ##gpa= sum of gpas in a while loop
            y=y-1                              ##Value of y is decreased stop loop from running continously

    ###display table
    data = {"Course no":z, "Course Name": mycourse, "Grades":engrades,  "Credit hours":credit,}        ## data= mycourse array + engrades array + credit array
    col_names = ["Course No","Courses names", "Grades", "Credit hours"]                 ##define header names
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid", )) ## Forming table of enetering courses and their grades, and their creit hours
    if gpas>0:                                                      ##condition (gpas>0)= Allow this code to run only if individual gpa(gpas) of course >0 
        sgpa=(gpa)/totalch        ##sgpa= overall gpa of courses (out of while loop)
        print("Want to calculate CGPA?")
        dec1=str(input("Yes/No:   "))                               ##Allowing user to decide whether to calculate CGPA or not
        if dec1=="yes" or dec1=="Yes":                              ##Code will run only when user allows it
            prevgpa=float(input("Enter previous semester gpa: "))   ##Taking previous semester gpa as input from user
            cgpa=(prevgpa+sgpa)/2                                   ##Calulting CGPA
            print("GPA is: ", sgpa)                                 ##Printing GPA of all courses
            print("CGPA is: ", cgpa)                                ##Printing CGPA
        else:
            print("GPA is: ", sgpa)                                 ##Printing GPA of all courses
elif dec=="No" or dec=="no" or dec=="NO":
    print("Okay")

else:
    print ("Incorrect input")

    
