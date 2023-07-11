#building a calculator
num1=float(input("Enter first number: " ))
op=(input("Enter operator: " ))
num2=float(input("Enter second number: " ))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)    
else:
    print("Invalid operator")

#dictionary
#dictionary is a special structure in python which allows us to store information in key value for eg. JAN=January
MonthConversions={
    "JAN":"January",
    "FEB":"February",
    "MAR":"March",
    "APR":"April",
    "MAY":"May",
    "JUN":"June",
    "JUL":"July",
    "AUG":"August",
    "SEP":"September",
    "OCT":"October",
    "NOV":"November",
    "DEC":"December"
}
print(MonthConversions["FEB"])
print(MonthConversions.get("SOP","404"))
#get function can be used to assign a default value to a new key
#while loop
#while loop is used to loop through and execute a block of code multiple times
i=1
while i<=50:
    print(i)
    i+=1
print("Done with loop")