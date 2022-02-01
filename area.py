#Python program to print area of the circle
pi=3.142
r=float(input("Enter the radius of the circle r :"))
a=pi*r*r
print("Area of the circle = ",a)

#Extract the extension of the file
fileName=input("Write the fileName")
file_extns=fileName.split(".")
print("The extension is"+repr(file_extns[-1]))

