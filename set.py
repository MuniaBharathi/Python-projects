#create and print a dict
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
    }
print(thisdict)

#create a set
thisset={"apple","banana","cherry"}
print(thisset)


#sorted function
questionSet={2,5,1,10}
descsort=sorted(questionSet)
print("Sorting question Set in desending= ",descsort)


#filename extension
fileName=input("Write the fileName")
file_extns=fileName.split(".")
print("The extension is"+repr(file_extns[-1]))

