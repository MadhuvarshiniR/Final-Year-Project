import os
classes = next(os.walk(os.getcwd()+'\\gestures\\train'))[1]  
index = 0
word_dict ={}

while index<len(classes):
    word_dict[index] = classes[index]
    index+=1


print(classes)
print(word_dict)