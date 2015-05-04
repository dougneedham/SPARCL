# SPARCL
To run this code the command is: 
cat filename | ./parser.awk | sort | ./reducer.py

To do a grouping of a number of columns together to demonstrate uniqueness the command would be: 

cat filename | ./parser.py 2 3 4 | sort | ./reducer.py

Output is a counter of unique values
