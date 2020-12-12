list_1={"hello","konichiwa","namaste","randomsomthing"};
#this is code which is made to understand how the list funtions work.
length_of_lsit=len(list_1)
#the above function calculates the length of the above list
max_in_the_list=max(list_1)
#the above fuctions will give us the of the biggest element in the list
min_int_the_list=min(list_1)
#the above functtion will give the minimum thing in the list
copylist=sorted(list_1)
#the above function will pass a copy of the loriginal list which is sorted in a perticular order
new_str="\n".join(list_1)
print("the length of the list is {}" .format(length_of_lsit))
print("the max element in the list is{}".format(max_in_the_list))
print("the min element in the string is {}".format(min_int_the_list))
print("the sorted list is as follows{}".format(copylist))
print("the new list with word in different line is\n{}".format(new_str))

