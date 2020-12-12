word_counter=["library","hills","trees","shaders","fog", "clif", "dual sword", "dual ", "seas"]
word={}
for i in word_counter:
    if i not in word:
        word[i]=1
    else:
        word[i]+=1
print(word)
