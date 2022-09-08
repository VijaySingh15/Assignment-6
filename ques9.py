x=int(input("Enter year :"))
if x%400==0:
    print("Given year is leap year")
elif x%100!=0 and x%4==0:
    print("Given year is leap year")
else:
    print("Given year is not leap year")
