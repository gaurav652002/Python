a=input("please enter the character you want to  check:")
if a==a.lower():
    print("the letter is in upper case")
elif a==a.upper():
    print("the character is in lower case")
elif a>=0 and a<=9:
    print("the character is a number")
#print("since special character have no upper or lower case senerio it will treat them according to the first condition, so it will not work fir special charcters")
