file1=open("simple.txt",'w')
a=input("Enter text to write to file:")
writing_file=file1.write(a)
file1.close()
print("Data successfully written to simple.txt\n")


file1=open("simple.txt",'a')
a=input("Enter additional text to append:")
appending_file=file1.write(a)
file1.close()
print("Data successfully appended\n")

file1=open("simple.txt",'r')
print("final content of simple.txt: ")
reading_file=file1.read()
print(reading_file)
file1.close()

OUTPUT
PS C:\Users\SANIYA\OneDrive\Desktop\dodothecoder> & "C:/Program Files/Python313/python.exe" c:/Users/SANIYA/OneDrive/Desktop/dodothecoder/4task2.py
Enter text to write to file:hello
Data successfully written to simple.txt

Enter additional text to append: lenovo
Data successfully appended

final content of simple.txt:
hello lenovo

