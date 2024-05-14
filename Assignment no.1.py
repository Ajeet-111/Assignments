#Q.1 -  How do you concatenate two strings in Python?

print("\nQ.1 answer:")

str1="My name is "
str2="Ajeet Singh."
print(str1 + str2)

# Q.2 - What method would you use to convert a string to lowercase in Python? 
print("\nQ.2 answer:")

str3="THIS IS A STRING."
print(str3.lower())

# Q.3 - How can you find the length of a string in Python? 
print("\nQ.3 answer:")

str4="fourth string"
print(len(str4))

# Q.4 - Remove the white space from left side of given string,  st = “       hello jecrc      " Remove the white space from left side of given string. 
print("\nQ.4 answer:")

st = "          hello jecrc          "
print(st.lstrip())

# Q.5 - What is the difference between the "insert()" and "append()" methods when adding elements to a list in Python, give an example by coding. 
print("\nQ.5 answer:")

list1=[1, 'jecrc', 2.5, True]
list1.append(50) # it adds an element at the last of the list.
print(list1)

list1.insert(2, 'college')
print(list1) #it adds an element at your desired location