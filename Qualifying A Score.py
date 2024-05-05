# Calculating the score of a student:

# asking for the score of any major:
a= float(input("please enter your score:"))

# Qualifying the score:
if 0<a<=9.9:
    print("Fail");
elif 10<=a<15:
    print("Good");
elif 15<=a<18:
    print("Very Good");
elif 18<=a<=20:
    print("Excellent");
else:
    print("Invalid Grade21");