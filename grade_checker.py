# Author: Nthabiseng Maya

"""
This program reads the student's practical and theory marks and convert each to its weighted mark like if the student passed 40% and above on practical and if the student passed 60% an above on theory the adds both assessments and examine whether the student has indeed passed or failed or has reached the pass mark of 50
"""

# it reads both marks and convert the mark into whole numbers
practical_score = int(input("Enter your Practical Assessment score: "))
theory_score = int(input("Enter your Theory Exam score: "))

# working out the part of the final mark that comes from the practical mark that weigh 40%
practical_mark = practical_score / 100 * 40

# working out the part of the final mark that comes from the theory exam that weigh 60%
theory_mark = theory_score  / 100 * 60

# combining the two weighed marks from two exams to get the final mark out of 100
total_mark = practical_mark + theory_mark

# Deciding the outcome so 50 or more is pass then any mark that is less than 50 is a fail
if total_mark >= 50:
   student_status = "You passed. Well done,"
else:
    student_status = "You failed."

# diplaying the breakdown and the total or final outcome
print("Your Practical score is: ", practical_score, " and your mark(40% of the total is: ", int(practical_mark))
print("Your Theory score is: ", theory_score, " and your mark(60% of the total is: ", int(theory_mark))
print("Your total mark is: ", int(total_mark))
print("Your status " + student_status)
