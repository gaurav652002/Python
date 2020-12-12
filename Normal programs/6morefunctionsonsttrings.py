verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print("the length of the the strings{}".format(len(verse)))
print("the index of the first occurance of the {}".format(verse.find('and')))
print("the last index of the lasr occurrence ofthe word \'you\'is{}".format(verse.rfind('you')))
print("the count of occurrance of the word you in the verse is{}".format(verse.count('you')))