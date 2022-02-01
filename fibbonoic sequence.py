#Fibbonic series
nums=int(input("Enter any number :"))
n1,n2=0,1
sum=0
if nums<=0:
    print("Please enter number greater than 0")
else:
    for i in range(0,nums):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2

