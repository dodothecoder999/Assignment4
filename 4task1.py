try:
    file1=open("simple.txt",'r')
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
   print("The sample file was not found")
finally:
   print("Continue with this code")

OUTPUT
PS C:\Users\SANIYA\OneDrive\Desktop\dodothecoder> & "C:/Program Files/Python313/python.exe" c:/Users/SANIYA/OneDrive/Desktop/dodothecoder/4task1.py
hello
Welcome to python programming
Continue with this code


   
