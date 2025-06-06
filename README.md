# Assignment4
#a program for adding and reading content form a file

file1 = open('sample.txt','w') #for writing contents in a new text file
writing_file = file1.write('Line 1: This is my first python file')
#print(writing_file)
file1.close()

#file1 = open('sample.txt','r') #for reading contents from sample.txt
#reading_file = file1.read()
#print(reading_file)
#file1.close()

file1 = open('sample.txt','a') #for appending data in file sample.txt
writing_file = file1.write(' \nLine 2: This is appended data in my file sample.txt')
#print(writing_file)
file1.close()

file1 = open('sample.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
