try:
    file1=open("simple.txt",'r')
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
   print("The sample file was not found")
finally:
   print("Continue with this code")


   