# GPA and CGPA Calculator 

This code is a GPA (Grade Point Average) and CGPA (Cumulative Grade Point Average) calculator written in Python. It allows users to input their course grades and credit hours to calculate their GPA for the current semester. If the user provides their previous semester's CGPA, the code can also calculate their new CGPA after considering the current semester's GPA.

## Dependencies

Before running the code, make sure you have the `tabulate` library installed. If not, you can install it using `pip`:

```
pip install tabulate
```

## Usage

1. Run the script in a Python environment (e.g., IDLE, command line, or any Python IDE).

2. The script will prompt you with the question: "Do you want to calculate GPA?" Enter "Yes" or "No" (case-insensitive) to proceed.

3. If you choose "No," the script will display "Okay" and terminate.

4. If you choose "Yes," the script will display a table containing grades and their corresponding credit points.

5. The script will then prompt you to enter the number of courses for which you want to calculate the GPA.

6. For each course, the script will ask for the following inputs:
   - Course name: Enter the name of the course.
   - Credit hours: Enter the number of credit hours for the course (must be greater than 0).
   - Grade: Enter the letter grade obtained for the course (e.g., A, B+, B, etc.).

7. After entering the details for all courses, the script will display a table showing the entered course data, including course number, name, grade, and credit hours.

8. The script will calculate the GPA for the current semester based on the entered course information.

9. If the GPA calculation is successful (i.e., all grades and credit hours are valid), the script will ask, "Want to calculate CGPA?" Enter "Yes" or "No" (case-insensitive) to proceed.

10. If you choose "No," the script will display the GPA for the current semester and terminate.

11. If you choose "Yes," the script will prompt you to enter your previous semester's CGPA.

12. The script will calculate the new CGPA by considering the current semester's GPA along with the entered previous semester's CGPA.

13. Finally, the script will display both the GPA for the current semester and the calculated CGPA.

   Enjoy calculating your GPA and CGPA using this simple Python script!
