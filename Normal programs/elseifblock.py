#this is program to display the working  of a else if block with boolean values
points =174
prize= None
if points<=50:
    prize="wooden rabbit"
elif points>150 and points<=180:
    prize="wafer-thin mint"
elif points>180 and points <=200:
    prize="penguin"
#test with the original value if none of the above case matches
if prize:
    result="Congratulations! You've won a {}".format(prize)
else:
    result="Oh dear, no prize this time."

print(result)