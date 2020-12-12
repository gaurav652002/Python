tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for tokens in tokens:
    if tokens[0]=="<" and tokens[-1]==">":
        count +=1
    

print(count)