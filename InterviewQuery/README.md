##Interview Query
    https://www.interviewquery.com/

### count_file_lines.py
Let's say you're given a huge 100 GB log file. You want to be able to count how many lines are in the file. 

Write code in Python to count the total number of lines in the file.
    
    create function with <filename> as argument 
        open file 
        initialize count variable
        initialize buffer size
        read first buffer size part of file
        iterate through the file piece by piece counting lines by counting '\n'
        return count

