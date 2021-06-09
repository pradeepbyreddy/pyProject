import sys
import os
counter=0
listA=[2,'words','name','number','SSN']
for w in listA:
    counter+=1
    print(w, len(str(w)))
print("length of a list is" , counter)
