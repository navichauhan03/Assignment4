#a program for adding and reading content form a file

file1 = open('sample.txt','w')
writing_file = file1.write('Line 1: This is my first python file')
#print(writing_file)
file1.close()

#file1 = open('sample.txt','r')
#reading_file = file1.read()
#print(reading_file)
#file1.close()

file1 = open('sample.txt','a')
writing_file = file1.write(' \nLine 2: This is appended data in my file sample.txt')
#print(writing_file)
file1.close()

file1 = open('sample.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()