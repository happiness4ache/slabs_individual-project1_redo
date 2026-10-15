# Author: Nthabiseng Maya

EDGE CASE & ANALYSIS 
--------------------

1) INVALID INPUT TYPES(text input e.g "abc" )
   ------------------------------------------
-the program accepts two marks, one for practical and one for theory. It adds the marks together to calculate the total and checks whether the student's results are 50 or higher
-if the user enters text such as "abc" instead of a number, the program cannot convert the input into an integer using int() so that means it will cause a Value Error which is a type of a Runtime Error

2) INVALID INPUT RANGE
  --------------------
-the program should only accept marks between 0 and 100.If a user enters a number such as 150 or maybe a negative number like -69, the input is outside the allowed range and the allowed range is between 0 and 100, even though these values are numbers but they are not valid marks so this is a logic error because the program needs to reject marks that fall outside the allowed limit 

3) ERROR CATEGORIES
  -----------------
-the program may face or maybe encounter different types of errors depending on the input entered 
Runime Error(Value Error)- this error occurs when the user enters text such as "abc" that cannot be converted into an integer
--------------------------
Logic Error- this occurs when the program accepts or maybe processes a mark outside the allowed range of 0 to 100 which can lead to an incorrect results
-----------

4)TYPE CASTING AND RANGE VALIDATION 
  ---------------------------------
-type casting is the process of converting a value from one data type to another, so in this program the int() function converts a number input from a string into an integer, for example if the user enters "82" the program converts it into the number 82 with no quotation marks and continue with the calculations but entering "abc" causes a Value Error because the text cannot be converted into an integer
-Range validation checks whether the entered marks are within the allowed limits of 0 to 100 so if the user enters a number like 150 or -69 then the program should identify the mark as invalid and prevent it from being used in the calculation
-using type casting and range validation together helps the grade checker handle inputs correctly.type casting also converts numerical text into integers while range validation ensures that the marks are within the allowed limits so this checks helps to prevent invalid inputs from affecting the student's total mark whether is a pass or fail result/mark  
